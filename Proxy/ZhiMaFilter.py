# -*- coding: utf-8 -*-
# __author__ = "zok"  362416272@qq.com
# Date: 2019-04-30  Python: 3.7

import requests
import json
import datetime
import redis
import time
from dateutil.parser import parse


class ZhiMaPool(object):
    """
    芝麻代理按次提取(非套餐)代理IP
    """

    # 远程服务器redis 请自行配置
    # pool = redis.ConnectionPool(host='127.0.0.1', port=6379, db=10, password='', decode_responses=True)
    pool = redis.ConnectionPool(host='127.0.0.1', port=6379, db=1)  # 本地redis
    r = redis.Redis(connection_pool=pool)

    def __init__(self, key, ttl=1000):
        """
        init zhima
        :param key: ZhiMaProxy    http://h.zhimaruanjian.com/pay/
        :param ttl:  Set survival time | seconds
        """
        self.key = key
        self.ttl = ttl

    def get_balance(self, count, total):
        """
        get balance from web api
        """
        balance_url = 'http://web.http.cnapi.cc/index/index/get_my_balance?neek=66439&appkey={key}'.format(key=self.key)
        response = json.loads(requests.get(balance_url).text)
        if response.get('success'):
            print('\033[1;34m余额:%s ,提取%s个\033[0m' % (response.get('data').get('balance'), str(count)))
            if total != count:
                print('\033[1;31m由于剩下存活时间过短弃用%s个\033[0m' % str(total-count))
        else:
            print(response.get('msg'))

    def get_ip(self, count=1, time=1, ip_type='1'):
        """
        get proxy ip and port
        """
        ip_type = '11' if ip_type == 'https' else '1'  # http(default) & https

        get_url = 'http://webapi.http.zhimacangku.com/getip'

        params = {
            'num': str(count),
            'type': '2',
            'pro': '',
            'city': '0',
            'port': ip_type,
            'time': time,  # 1=5m~25m   2=25m~3h  3=3h~6h  4=6h~12h
            'ts': '1',
            'ys': '0',
            'cs': '0',
            'lb': '1',
            'sb': '0',
            'pb': '4',
            'mr': '1',
            'regions': ''
        }
        response = requests.get(get_url, params=params)
        self.parse(response.text)

    def parse(self, json_data):
        """
        parse response json
        """
        count = 0
        ret_dict = json.loads(json_data)
        if ret_dict.get('success'):
            nodes = ret_dict.get('data')
            for node in nodes:
                end_time = self.get_end_time(node.get('expire_time'))
                if not end_time:
                    """该域名存活时间过短，已弃用"""
                    continue
                self.save_to_redis(node.get('ip')+':'+str(node.get('port')), end_time)
                count += 1

            self.get_balance(count, len(nodes))  # get balance
        else:
            if ret_dict.get('code') == 113:
                msg = ret_dict.get('msg')
                ip = msg[2:msg.rfind('设')]
                if ip:
                    print('\033[1;35m初次启动，芝麻代理初始化中\033[0m')
                    self._init(ip)
            else:
                print('获取代理失败:', ret_dict)

    def get_end_time(self, parse_time):
        """
        time transformation
        """
        a = parse(parse_time)
        b = parse(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        results = (a - b).total_seconds()
        if results > self.ttl:
            return int(time.mktime(time.strptime(parse_time, "%Y-%m-%d %H:%M:%S")))
        else:
            return

    def save_to_redis(self, proxy, expire):
        """
        proxy save to redis，default score is expire time
        """
        if not self.r.zscore('ZhiMa', proxy):
            return self.r.zadd('ZhiMa', {proxy: expire})

    def _init(self, set_ip):
        """
        Initialize the proxy
        """
        url = 'http://web.http.cnapi.cc/index/index/save_white?neek=66439&appkey={key}&white={local}'.format(
            key=self.key, local=set_ip)
        response = requests.get(url=url)
        code = json.loads(response.text).get('code')
        if code == 0:
            print('\033[1;35m初始化成功, 请重新启动\033[0m')
        else:
            print('设置失败等两秒再试')


zm_key = input('填入你的芝麻代理Key')
num = input('提取个数')
obj = ZhiMaPool(zm_key)
obj.get_ip(int(num))
