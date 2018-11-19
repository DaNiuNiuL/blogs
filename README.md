#验证模块包含
* User   用户数据表包含：username password Email is_active
* Group  用户组
* Permission 存放用户和组的权限


#一个登录的视图
* 通过用户提交的表单获取用户名和密码
* 将用户名和密码与数据库中的数据进行匹配
* 检查用户是否处于活跃状态
* 通过在HTTP请求上附加session，让用户进入登录状态


#使用消息框架
* django.contrib.messages 和MessageMiddleware 共同构成了消息系统


# sorl-thumbnail
* 这个模板采用两种方法显示缩略图
* 一个是提供了一个新的标签模板{% thumbnail %}
* 二是基于ImageField自定义的图片字段


#使用jQuery发送Ajax请求
* AJAX Asynchronous javaScript and XML
* xml 不是必须采用的格式，还可以是json和html或者纯文本