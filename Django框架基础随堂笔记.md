```

```

```
MVT 流程

前端 发请求--- 网址 路由 url--查找资源路径
后端--wsgi协议--django框架程序----判断路由对应是哪个 功能函数 views-----接收请求- 处理请求----返回响应对象给前端 

没有虚拟环境  你也是可以写代码的 django

# 1.使用django 创建项目 django-admin startproject zdemo
# 2.cd zdemo
# 3.创建子应用 python manage.py startapp users
# 4.注册子应用
# 5. 设置路由 ---找功能函数
# 6. 设置总路由--子路由--找功能函数
```

### Django工程搭建

```
1.开发环境
	1.1 开发语言：Python3.x
	1.2 开发框架：Django==2.2.5
	1.3 开发工具：PyCharm
	
2.系统环境
	2.1 VMware虚拟机
	2.2 ubuntu 16.04/18.04
	
3.Django框架介绍
	3.1 Web框架的意义
		Django框架属于Web框架的一种，帮助我们开发Web程序的，还有Flask、tornado、......
	3.2 Django框架的特点
		3.2.1 属于重量级框架，功能齐全并强大，
			默认具备了开发一个网站所需要的几乎所有组件。
		3.2.2 遵守了MVT设计模式，类似于MVC设计模式的思想。（各个功能模块之间相互分工，解耦）
			设计模式：
				他就是我们的前辈们在很久之前做开发时总结出来的解决某一系列问题的经验。
				比如：遇到了高耦合度的代码需要解耦的问题，我们可以选择前辈们总结的MVC设计模式
				设计模式是抽象的，不是具体存在的。他有很多种表现形式。
				凡是体现出了分模块去解耦的操作，我们都可以归为MVC设计模式的思想
			MVC设计模式：
				它是分工合作并解耦的典范。用来解决开发时分工不明确的问题。
				前后端开发都有MVC设计模式。
				后端的MVC：
					M-Model：访问操作数据库的模块
					V-View：数据展示层，处理数据的展示的
					C-Contorll：中央调度层，接收请求并处理响应，负责协调M和V的数据交互的
		3.2.3 M-Model：访问操作数据库的模块
		3.2.4 V-View：接收请求，处理业务逻辑，响应结果
		3.2.5 T-Template：渲染页面
		
4.虚拟环境
	4.1 为什么要创建虚拟环境？
		4.1.1 虚拟环境可以帮助我们搭建独立的python运行环境, 使单个项目的运行环境与其它项目互不影响
		4.1.2 这个效果就跟在学校里每个班级都有自己独立的教室是一样的，保证各自环境的独立性
		4.1.3 所以为了保证每个项目都有独立的运行环境，我们可以使用虚拟环境去实现
	4.2 如何创建虚拟环境？
		4.2.1 安装虚拟环境程序
			sudo pip install virtualenv
        	sudo pip install virtualenvwrapper
        4.2.2 创建py3的虚拟环境
        	mkvirtualenv -p python3 虚拟环境名称
	4.3 如何使用虚拟环境？
		4.3.1 查看已有虚拟环境
			workon 两次tab键
		4.3.2 切换虚拟环境
			workon 虚拟环境名称
		4.3.3 退出虚拟环境
			deactivate
		4.3.4 删除虚拟环境
            rmvirtualenv 虚拟环境名称
	4.4 如何在虚拟环境中安装工具包？
		4.4.0 先查看有哪些虚拟环境：Django框架安装在ubuntu操作系统的虚拟环境中的
            workon 两次连续tab键
            你们的ubuntu里面已经准备好了虚拟环境了
            然后切换到对应的虚拟环境：workon 虚拟环境名字
		4.4.1 安装框架或扩展
			pip install 框架==版本、包名称==版本
			pip install django==2.2.5
		4.4.2 安装位置：
			"~/.virtualenvs/虚拟环境名称/lib/python版本/site-packages"
		4.4.3 查看安装结果
			pip list
		
5.创建Django工程
	5.1 进入到虚拟环境：workon 虚拟环境名字
	5.2 准备项目工程文件目录，确定项目工程的位置，自己选
	5.3 创建Django工程：django-admin startproject 工程名字
	5.4 使用PyCharm打开项目工程，需要在PyCharm的设置中切换对应的虚拟环境
	5.5 在虚拟环境中进入到项目工程文件目录：
		python manage.py runserver (默认的)
		python manage.py runserver ip:端口
	5.6 默认访问：http://127.0.0.1:8000
	
6.配置Django工程
	6.1 位置：在项目同名文件目录下，名字叫做settings.py
	6.2 作用：用来配置项目的，可以通过配置文件向项目中传递额外的数据（开发中经常需要添加配置信息的）
	
7.创建并注册子应用
	7.1 子应用的作用：管理项目中划分出来的模块，可以让模块间降低耦合度，并且可以复用的
	7.2 子应用的创建：
		python manage.py startapp 子应用名字
		或者
		django-admin startapp 子应用名字
	7.3 子应用的注册：在INSTALLED_APPS配置项中，以子应用的名字直接注册即可
```

### 视图

> 学习目标：
> - 学会如何定义视图（函数视图和类视图）
> - 学会定义路由去匹配请求地址中的路径
> - 学会如何在视图中获取前端发送的请求数据
> - 学会如何在视图中给前端响应不同的数据
> - 学会Cookie和Session的使用
> - 中间件

```
0.视图 View：
	作用：用于接收请求，处理业务逻辑，并响应结果的。(响应结果：HTML页面，JSON，......)
	案例：用户访问 GET http://127.0.0.1:8000/users/register/，我们假装给他返回一个注册页面
	
1.定义函数视图
	1.1 函数视图定义的位置：子应用.views.py
	1.2 views.py文件的作用：实现子应用(模块)对应的功能的地方
	1.3 定义函数视图
		1.3.1 函数视图他是一个标准的Python函数
		1.3.2 函数视图中必传参数为：request，用于接收用户发送的请求报文
		1.3.3 函数视图中必须返回响应对象：用于构造响应报文，并响应给用户
		def register(request):
            """注册视图
            :param request: 包含了请求信息的请求对象
            :return: 响应对象
            """
            return HttpResponse("假装这是个注册页面")
    1.4 定义好视图后，需要思考的问题：
    	1.4.1 该视图何时被调用？
    		当用户向设计好的地址发起请求时，我们就需要调用对应的视图。
    		作为后端需要去设计哪个地址对应哪个视图，然后再根据自己的设计去定义路由
    	1.4.2 该视图如何被调用？
    		我们需要定义路由去匹配请求地址中的路径，根据匹配结果调用对应的视图
    		
2.函数视图绑定路由
	2.1 路由类似于我们网购时填写的收货地址，帮助快递员找到我们（帮助用户找到要访问的视图）
	2.2 路由的作用：就是为了帮助用户通过请求地址找到要访问的视图
	2.3 路由的定义：
		2.3.1 后端程序员可以决定并设计哪个地址对应哪个视图
		2.3.2 路由的入口：ROOT_URLCONF = '工程同名目录.urls'
		2.3.3 总路由样式列表：
			urlpatterns = [
				path('', include('users.urls')), # 一个子应用对应一个它的总路由
			] 
		2.3.4 子路由样式列表：
			urlpatterns = [
				path('users/register/', views.register), # 一个视图对应一个子路由
			]
	2.4 路由访问：
		启动的Django程序后，在浏览器输入 http://127.0.0.1:8000/users/register/ 即可
		
3. 定义类视图
	3.1 类视图定义的位置：子应用.views.py
	3.2 views.py文件的作用：实现子应用(模块)对应的功能的地方
	3.3 定义类视图
		3.3.1 类视图它是一个标准的Python类
        3.3.2 类视图需要继承自Django提供的父类视图View
        3.3.3 在类视图中，
            1. 需要定义跟请求方法同名的函数来对应不同请求方式
            2. 在请求方法同名的函数中，还必须定义一个接收请求的参数（同函数视图）
            3. 在请求方法同名的函数中，还必须返回一个响应对象（同函数视图）
		class RegisterView(View):
            """用户注册类视图"""
            def get(self, request):
                """处理GET请求，返回注册页面
                :param request: 请求对象，包含了请求报文信息
                :return: 响应对象，用于构造响应报文，并响应给用户
                """
                return http.HttpResponse('这里假装返回注册页面')

            def post(self, request):
                """处理POST请求，实现注册逻辑
                :param request: 请求对象，包含了请求报文信息
                :return: 响应对象，用于构造响应报文，并响应给用户
                """
                return http.HttpResponse('这里假装实现注册逻辑')
	3.4 类视图的访问
		3.4.1 总路由样式列表：
			urlpatterns = [
				path('', include('users.urls')),
			] 
		3.4.2 子路由样式列表：
            urlpatterns = [
                path('users/register/', views.RegisterView.as_view()),
            ]
		3.4.3 路由的访问
        	GET http://127.0.0.1:8000/users/register/
        	POST http://127.0.0.1:8000/users/register/
4.提取用户发送的请求参数
	4.1 发送请求参数方式的说明
		4.1.0 用户发送请求时携带的参数后端需要使用，而不同的发送参数的方式对应了不同的提取参数的方式
		4.1.1 查询字符串参数：http://www.meiduo.site/list/115/1/?sort=price
		4.1.2 请求体参数：POST表单或JSON数据（请求体一般用于传递隐私数据，注册或登陆数据......）
		4.1.3 路径参数：http://www.meiduo.site/detail/2/
		4.1.4 请求头参数：user-agent 客户端信息（用的少）
	4.1 查询字符串参数：http://127.0.0.1:8000/test/18/?name=zxc&sort=price
		name = request.GET.get('name')
        sort = request.GET.get('sort')
	4.2 请求体参数：POST表单或JSON数据
		4.2.1 说明：
			浏览器的地址栏只能发送GET请求，不能发送非GET请求（POST, PUT，DELETE）
			所以在浏览器的地址栏中无法演示POST请求的
		4.2.2 在学习时，我们可以借助一个软件来帮助我们发送模拟的请求，postman，需要先安装
		4.2.3 获取POST表单数据：request.POST
		4.2.4 获取JSON数据：request.body
	4.2 路径参数：http://127.0.0.1:8000/test/18/
		path('test/<int:num>/', 视图)
		或者
		re_path(r'^test/(?P<num>\d+)/$', 视图)
```

```
能够说出Django框架的作用和特点X
写的少 跑的快 做的多; web应用, MVC设计模式, 重量级

能够说出MVT设计模式的核心思想X
M model
V 视图
T template 

能够使用虚拟环境安装Django框架X
mkvirtualenv -p python3 虚拟环境的名字
在虚拟环境里面--pip install django

能够使用命令创建Django工程和子应用X
django-admin startproject  工程名字
cd 工程目录
python manage.py startapp 应用名/ djdango-admin startapp 应用名

能够在Django工程中定义视图和路由X
总路由--视图函数
项目--同名目录--urls.py(总路由)--path('login/', views.index)---子应用--users.views.py--
def index(request):
	return http.HttpResponse('字符串')
	
总路由--子路由--视图函数
项目--同名目录--urls.py(总路由)--path('',include('users.urls'))---子应用- 新建urls.py==path('users/register/', views.register)---users.views.py--
def register(request):
	return http.HttpResponse('字符串')

```

