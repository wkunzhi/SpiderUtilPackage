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
- [x] [代理IP-芝麻代理-提取过滤器](https://github.com/wkunzhi/SpiderUtilPackage/tree/master/Proxy)
- [x] [代理IP-提取redis存活IP器](https://github.com/wkunzhi/SpiderUtilPackage/tree/master/Proxy)


-------


# directory tree



```
  
.
├── Proxy                               //      代理工具包 
│   ├── ZhiMaFilter.py                  // 芝麻代理ip清洗工具
│   └── Demo.py                         // 基于上个工具提取redis存活IP器
└── README.md

```


<hr>


# 说明

- [x] **芝麻代理过滤**

> 这是一个付费的代理ip商！但是有的时候提取到的代理ip存活时长较短，该工具可以过滤掉所剩时间不多的ip，将其添加到redis库中，时间到期后ip会清空。
在需要使用代理ip的时候只需要从直接的redis中推出可用IP即可

**含2个文件**
1. IP提取过滤器
2. 提取redis存活IP器

![image](https://zok-blog.oss-cn-hangzhou.aliyuncs.com/images/%E8%8A%9D%E9%BA%BB3.png)




------
