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
- [x] [代理IP-简单实用的付费代理池清洗监控器](https://github.com/wkunzhi/SpiderUtilPackage/tree/master/Proxy)
- [x] [代理IP-CleanProxyPool的客户端Demo](https://github.com/wkunzhi/SpiderUtilPackage/tree/master/Proxy)


-------


# directory tree



```
  
.
├── Proxy                               //      代理工具包 
│   ├── CleanProxyPool.py               // 芝麻代理ip清洗工具
│   └── Demo.py                         // 基于上个工具提取redis存活IP器
└── README.md

```


<hr>




# **付费代理池清洗监控器**

[**博客传送门**](https://blog.zhangkunzhi.com/2019/05/02/%E6%90%AD%E5%BB%BA%E4%B8%80%E4%B8%AA%E8%B6%85%E7%AE%80%E5%8D%95%E7%9A%84%E5%AE%9E%E7%94%A8%E7%9A%84%E9%AB%98%E5%8F%AF%E7%94%A8%E4%BB%98%E8%B4%B9IP%E6%B1%A0/index.html)

> 爬虫经常会用到代理ip，其中有很多收费ip，但是如何在scrapy中，高效使用这些ip是一个比较麻烦的事情，在这里基于[芝麻代理ip](http://h.zhimaruanjian.com/pay/)做一个代理池监控器，首先整理我们的需求

## 整理需求
> 芝麻付费代理 取ip是不要钱，只有使用才收费，针对这个特点，可以让我们代理池24小时始终保持指定数量的ip即使没有使用

- [x] 需要监控**ip是否过期**，如果已经过期就从池中删除
- [x] 监控访问目标网址的**成功率**，将成功率低的自动剔除
- [x] 让ip池长期保持设定的**ip数量**，以便随时取用


## 服务端
- [x] 程序需要在服务端24小时运行
- [x] 实时监控，默认2秒频率 `apscheduler模块`
- [x] `redis的有序集合`积分板功能作为ip储存，所以程序最好是放于redis同服务器或者同内网上保障实时读写效率
- [x] 提取IP的时候，有效存活时间过短的自动放弃(不入库)自动筛选
- [x] **监控内容**：
    - 扫描每个IP过期时间，到期删除
    - 总个数小于预设值就申请新的IP且值初始ip质量分=10
    - 积分 = 'ip质量分' + '到期时间戳'  例如：  101556616966  后面10位是时间戳，前面是分数10。
- [x] **注意**： 分数加减只是对前面2位进行加减，后面10位是时间戳用来比对时间

## 爬虫端
- [x] 中间键配置代理ip从redis中 random.choice()出ip
- [x] 访问成功 质量分数+1 访问失败 质量分数-1

> 这样一来一个简易版的IP池管理工具就搞定了，池中一直会保持可用的**新鲜IP**

------


## 使用说明
```bush
pip3 install redis
pip3 install apscheduler
pip3 install reuqest
pip3 install python-dateutil
```

- python 3.7.2
- redis 5.0.4
- apscheduler 3.6.0

1. 首先登陆你的芝麻代理后台管理，找到自己的key如图
    ![key位置](https://www.zhangkunzhi.com/images/芝麻1.png)

1. 在代码下方配置key
    ![key位置](https://www.zhangkunzhi.com/images/填入芝麻key.png)
    
1. 在代码中配置 redis库连接 **默认链接的本地**
    ![key位置](https://www.zhangkunzhi.com/images/代理模块.png)
    
1. 启动程序
    > 如果在服务端可以使用后台运行命令
    `nohup python3 ProxyPool.py >my.log &`
 
1. 第一次启动芝麻代理会绑定你的ip白名单，稍等片刻就会开始提取     
    
    ![key位置](https://www.zhangkunzhi.com/images/提取ip.png)
    
1. 链接redis可以看到ip池了，大功告成
    ![key位置](https://www.zhangkunzhi.com/images/20个ip.png)
    
1. 后续在使用代理ip时，根据访问结果对代理ip积分增减即可，后续会更新这个Demo继续关注Github即可。[**传送门**](https://github.com/wkunzhi/SpiderUtilPackage)
    
    
## 额外配置
- 可以自由配置，代理池上线值(默认20),实例化时配置即可
    ```python
    zm = ZhiMaPool('key', ip_sum=100)
    ```
- 可以自由配置，只取可用时间xx以上的ip(默认1号套餐下的1000秒以上),实例化时配置即可
    ```python
    zm = ZhiMaPool('key', ttl=1000)
    ```
- 还可以配置 每次提取数、提取套餐类型、提取ip HTTP或者HTTPS或者Sockets
 


<hr>
