# SpiderUtilPackage


![](https://zok-blog.oss-cn-hangzhou.aliyuncs.com/ico/python-3.7-green.svg) 

不断增加更新中...

> 一些常用的方便爬虫工作的工具包


| Author  | Zok |
| --- | --- |
| Email | 362416272@qq.com  |
| BLOG | www.zhangkunzhi.com |


-------
## 工具表
- [x] [自动注册-验证短信接收器](https://github.com/wkunzhi/SpiderUtilPackage/tree/master/Register)
- [x] [代理IP-芝麻代理池监控器](https://github.com/wkunzhi/SpiderUtilPackage/tree/master/Proxy)
- [x] [代理IP-芝麻代理池客户端Demo](https://github.com/wkunzhi/SpiderUtilPackage/tree/master/Proxy)
- [x] [代理IP-讯代理池监控器](https://github.com/wkunzhi/SpiderUtilPackage/tree/master/Proxy)
- [x] [代理IP-讯代理池客户端Demo](https://github.com/wkunzhi/SpiderUtilPackage/tree/master/Proxy)


-------


# directory tree



```

.
├── Proxy                               //      代理工具包 
│   ├── ZhiMaProxyPool.py               // 芝麻代理ip清洗工具
│   ├── ZhiMaProxyUseDemo.py            // 芝麻代理池客户端使用Demo
│   ├── XDLProxyPool.py                 // 讯代理ip清洗工具
│   └── XDLProxyUseDemo.py              // 讯代理池客户端使用Demo
├── Register                            //      注册类工具
│   └── MessageCode.py                  // 异步验证短信接收器
└── README.md

```


<hr>




# 代理池清洗工具

[**博客传送门**](https://blog.zhangkunzhi.com/2019/05/02/%E6%90%AD%E5%BB%BA%E4%B8%80%E4%B8%AA%E8%B6%85%E7%AE%80%E5%8D%95%E7%9A%84%E5%AE%9E%E7%94%A8%E7%9A%84%E9%AB%98%E5%8F%AF%E7%94%A8%E4%BB%98%E8%B4%B9IP%E6%B1%A0/index.html)

> 爬虫经常会用到代理ip，其中有很多收费ip，但是如何在scrapy中，高效使用这些ip是一个比较麻烦的事情，在这里基于[芝麻代理ip](http://h.zhimaruanjian.com/pay/)做一个代理池监控器，首先整理我们的需求再对其代理质量进行管理，从而保持高效IP使用率




<hr>

# 验证码短信接收器

> 基于短信接收平台的异步短信接收器，最大并发上限 20，Python3.5+。
启动后会根据设置的异步并发数进行获取手机号码并监听短信接收情况（60秒） 超过60秒后会将未收到短信的手机号拉入黑名单，并是释放。

若要配置具体某个网站使用，还需开发对应的账号注册器，配合调用本短信接收器来达到自动注册账号的功能
