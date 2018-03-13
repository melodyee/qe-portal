##### 生产者和消费者模式
示意如图：

![AMQP](http://vision.internal.zerozero.cn:8070/files/producer.png)

解决问题：

* 解耦
* 异步

**Celery的架构**

Celery通过消息队列的方式解决任务在不同机器或进程间的调度

* 消息中间件（message broker） 
* 任务执行单元（worker）
* 任务执行结果存储（task result store）

#### 消息队列介绍

![AMQP](http://vision.internal.zerozero.cn:8070/files/amqp.png)

* Broker: 接收和分发消息的应用，RabbitMQ Server就是Message Broker。
* Exchange: 根据分发规则，匹配查询表中的routing key，分发消息到queue中去。常用的类型有：direct (point-to-point), topic (publish-subscribe) and fanout (multicast)。
* Binding: exchange和queue之间的虚拟连接，binding中可以包含routing key。Binding信息被保存到exchange中的查询表中，用于message的分发依据。
* Queue: 消息最终被送到这里等待consumer取走。一个message可以被同时拷贝到多个queue中。
* Connection: publisher／consumer和broker之间的TCP连接。断开连接的操作只会在client端进行，Broker不会断开连接，除非出现网络故障或broker服务出现问题。
* Channel: 如果每一次访问RabbitMQ都建立一个Connection，在消息量大的时候建立TCP Connection的开销将是巨大的，效率也较低。Channel是在connection内部建立的逻辑连接，如果应用程序支持多线程，通常每个thread创建单独的channel进行通讯，AMQP method包含了channel id帮助客户端和message broker识别channel，所以channel之间是完全隔离的。Channel作为轻量级的Connection极大减少了操作系统建立TCP connection的开销。
* Virtual host: 出于多租户和安全因素设计的，把AMQP的基本组件划分到一个虚拟的分组中，类似于网络中的namespace概念。当多个不同的用户使用同一个RabbitMQ server提供的服务时，可以划分出多个vhost，每个用户在自己的vhost创建exchange／queue等。


#### Celery整体架构图
![整体架构图](http://vision.internal.zerozero.cn:8070/files/celery.png)
