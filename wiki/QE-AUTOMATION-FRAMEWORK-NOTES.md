##自动化框架
###已有部分
* Django+Bootstrap框架开发（MTV）
	* 实现路由、基本页面、基础case组织逻辑等功能
* Server部署在apache上
* 使用Celery实现任务分发及结果存储

![基本结构](http://vision.internal.zerozero.cn:8070/files/base.png)
_________

###Django部分
* [开发环境部署](http://192.168.186.29/QE-Auto/QE-PORTAL/wikis/home)

_________

###服务器Apache部分

* MAC自带Apache
   * ```sudo apachectl -v``` 查看版本
   * ```sudo apachectl start``` 启动Apache
   * 进入/var/log/apache2 目录下查看Apache相关log

* mod_wsgi.so文件配置

The mod_wsgi package provides an Apache module that implements a WSGI compliant interface for hosting Python based web applications on top of the Apache web server.

   * 1）获取mod_wsgi.so文件方式如下：
       * brew install mod_wsgi 失败？ 不要担心，还可以通过如下两种方式
       * git clone  [mod_wsgi on Github ](https://github.com/GrahamDumpleton/mod_wsgi.git)后自己编译出so文件后（make install 会失败 无法copy至/usr/libexec下）
       * ```pip install mod_wsgi```，安装成功后到python安装目录下找到mod_wsgi.so，例如python2.7/site-packages/mod_wsgi/server/mod_wsgi.so

   * 2）将mod_wsgi.so文件放至/etc/apache2/modules下（其他目录也可），没有modules文件夹可以手动创建

   * 3）修改/etc/apache2/httpd.conf 文件，添加如下内容

```
LoadModule wsgi_module /etc/apache2/modules/mod_wsgi.so

WSGIScriptAlias / /Library/WebServer/Documents/QE-PORTAL/qe_portal/qe_portal/wsgi.py

WSGIPythonPath /Library/WebServer/Documents/QE-PORTAL/qe_portal

<Directory /Library/WebServer/Documents/QE-PORTAL/qe_portal/qe_portal>
        <Files wsgi.py>
                Order deny,allow
                Allow from all
        </Files>
</Directory>

Alias /media /Library/WebServer/Documents/QE-PORTAL/qe_portal/media
Alias /static /Library/WebServer/Documents/QE-PORTAL/qe_portal/static

<Directory /Library/WebServer/Documents/QE-PORTAL/qe_portal/static>
        Allow from all
</Directory>

<Directory /Library/WebServer/Documents/QE-PORTAL/qe_portal/media>
        Allow from all
</Directory>

<Directory /Library/WebServer/Documents/QE-PORTAL/qe_portal/automation/templates>
        Order Deny,Allow
	Allow from all
</Directory>

```

**遇到的两个问题**
	
* 1）WSGIScriptAlias / /Library/WebServer/Documents/QE-PORTAL/qe_portal/qe_portal/wsgi.py 前面的/ 表示web应用部署完成后的访问层级。如果设置成/qe-portal 则部署完成后的地址为http://ip:port/qe-portal/ 去访问

* 2）Alias /media /Library/WebServer/Documents/QE-PORTAL/qe_portal/media
Alias /static /Library/WebServer/Documents/QE-PORTAL/qe_portal/static

这两个地方 目录结尾的/ 一定要匹配上，不然会出现能显示页面 但是无bootstrap框架的问题，页面很难看

**项目中涉及的文件配置**

*  1）wsgi.py 添加如下内容
		
```
	import sys
	os.environ.setdefault("DJANGO_SETTINGS_MODULE", "qe_portal.settings")
	sys.path.append('/Library/WebServer/Documents/QE-PORTAL/qe_portal')
	sys.path.append('/Library/WebServer/Documents/QE-PORTAL/qe_portal/qe_portal')
```
		
* 2）settings.py 

```	
ALLOWED_HOSTS = ['localhost']  允许外界通过那个名称访问

e.g.
ALLOWED_HOSTS = [ 'qe-port', 'localhost', '127.0.0.1', '192.168.187.16'] 
```

写db时db.sqlite3遇到权限问题 ，执行以下命令设置用户组：

```
chown _www db.sqlite3 . 
```
Debug过程遇到的问题：

1. chmod修改db文件及其所在上级目录权限不好用，修改目录权限后反而不能cd 进去，在Mac中选择该文件，并查看Get Info面板中中修改权限为Read&Write后解决，奇怪！！

2. 步骤1仍然不好使，应该使用chown命令来设置用户为apache用户（默认是_www，可以查看httpd.conf文件）

	
另在我的机器上我的用户用管理员权限，可能屏蔽了一些权限问题，后期遇到再记录
	
其他环境 google，配置修改的文件不一样，内容差不多


* **重启服务器**

上述配置完成后，重启Apache server： apachectl restart，连接上面配置的ip和端口就可通过浏览器访问网站，例如[http://127.0.0.1:80/dashboard/](http://127.0.0.1:80/dashboard/)


_________

###任务分发Celery部分

**Celery介绍，消息队列介绍及架构图** [戳我！](http://192.168.186.29:4567/Celery-Introduction)


####安装RabbitMQ && Redis（MAC）

[RabbitMQ安装启动可参考](http://docs.celeryproject.org/en/latest/getting-started/brokers/rabbitmq.html)

1 安装启动RabbitMQ

```
1) brew install rabbitmq

2) rabbitmqctl add_user forward password

3) rabbitmqctl add_vhost ubuntu

4）rabbitmqctl set_permissions -p ubuntu forward ".*" ".*" ".*"

5）sudo rabbitmq-server
```


2 安装启动Redis

```
1) brew install redis
   Python support redis: sudo pip install redis
2）启动redis
进入安装目录/usr/local/Cellar/redis/4.0.7，执行./redis-server /usr/local/etc/redis.conf
或者 直接运行 redis-server /usr/local/etc/redis.conf

```

3 安装启动Flower

Flower 是一个 celery 的监控工具，它提供了一个图形用户界面，可以极大的方便我们监控任务的执行过程， 执行细节及历史记录，还提供了统计功能。

```
sudo pip install flower

Enter /home/qe-ops/qe-dev/QE-PORTAL/qe_portal

celery flower -A qe_portal --address=0.0.0.0 --port=5555

```

then browser: [http://localhost:5555](http://localhost:5555)


####RabbitMQ & Redis在项目中的配置

1）celery.py 中设置如下

```
app = Celery('qe_portal', backend='redis://qe-port:6380', broker='amqp://qe:1234@qe-port:5672')
```

2) Worker 

支持同时启动多个，在不同的PC端，也支持同一个PC上启动多个。

```
cd /home/qe-ops/qe-dev/QE-PORTAL/qe_portal (QE服务器地址)

celery -A qe_portal worker --concurrency=1 -l debug -Q web
```

#### 具体调用
```
task.py

@shared_task(queue="web")
def run_web_task(tc):


schdule.py

res = run_web_task.delay(case)


res = AsyncResult(item.task_id, app=app)
        tc_running = res.get(timeout=item.case.timeout, propagate=False)
        print "tc_running", tc_running
        item.ret_code = tc_running.ret_code
```