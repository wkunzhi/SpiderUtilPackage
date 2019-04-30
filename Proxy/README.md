# 概述
正常情况下花钱提取的ip（默认时长位5-25分钟） 该工具会过滤只收录20分钟以上存活时间的ip并入库到redis中，利用redis积分功能对代理ip进行管理

# 使用说明
> 次工具是针对芝麻收费代理，按次收费
### 获取API的Key

[**获取页面**](http://h.zhimaruanjian.com/getapi/)

![image](https://zok-blog.oss-cn-hangzhou.aliyuncs.com/images/%E8%8A%9D%E9%BA%BB1.png)

### 配置redis

在类中配置自己的redis链接
![image](https://zok-blog.oss-cn-hangzhou.aliyuncs.com/images/%E8%8A%9D%E9%BA%BB2.png)

### 运行启动即可


# 注意

- 默认是提取5-25分钟套餐的IP
- 默认全国提取
- 默认4位端口
- 默认360天去重

