# Django框架对接Mysql 数据库的 配置准备

###  1.开启mysql的数据库 服务--ubuntu--自动开启

### 2.登录mysql的客户端

```shell
mysql -uroot -pmysql

# 创建 数据库 django_demo---> 记得 utf-8
create database django_demo default charset=utf8;
```

### 3.在django项目中--settings.py--DATABASES

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': '127.0.0.1',  # 数据库主机
        'PORT': 3306,  # 数据库端口
        'USER': 'root',  # 数据库用户名
        'PASSWORD': 'mysql',  # 数据库用户密码
        'NAME': 'django_demo'  # 数据库名字
    }
}
```

### 4. ubuntu-特有的系统-必须安装一个软件--mysql链接

```shell
sudo apt-get install libmysqlclient-dev
```



###  可能会报的错

![1](./1.png)

![2](./2.png)

### 5.在python3的虚拟环境中--安装 第三方库--mysqlclient

```shell
workon 进入虚拟环境
pip install mysqlclient==1.4.6 -i https://pypi.tuna.tsinghua.edu.cn/simple/
```



# 1.ORM操作

#### 千万注意: 先配置成功 mysql 相关内容

### 1.创建模型类

```python
# models.py
class Stu(models.Model):
    # 主键默认创建  id --自增--唯一
    name = models.CharField(max_length=20, null=True)
    age = models.IntegerField()
    gender = models.BooleanField(default=False)

```

###  2.数据迁移--告诉ORM框架---让它 将模型类 迁移到mysql数据库中--生成一张表table

```shell
# 生成迁移文件
python manage.py makemigrations

# 迁移
python manage.py migrate
```

###  3. 添加测试数据

> 1.booktest-应用--models.py---创建 图书模型类和 英雄模型类

```python
class BookInfo(models.Model):
    """图书信息：演示一对多，一方"""
    btitle = models.CharField(max_length=20, verbose_name='书名')
    bpub_date = models.DateField(verbose_name='发布日期')
    bread = models.IntegerField(default=0, verbose_name='阅读量')
    bcomment = models.IntegerField(default=0, verbose_name='评论量')
    is_delete = models.BooleanField(default=False, verbose_name='逻辑删除')

    class Meta:
        """模型类的元类：用于修改、配置模型类对应的数据表"""
        db_table = 'tb_books'  # 自定义数据库表名

    def __str__(self):
        """定义每个数据对象的显示信息"""
        return self.btitle # 输出该模型数据对象时，只输出书名


class HeroInfo(models.Model):
    """英雄信息：演示一对多，多方"""
    # 确定性别字段的取值范围
    GENDER_CHOICES = (
        (0, 'female'),
        (1, 'male')
    )
    hbook = models.ForeignKey(BookInfo, on_delete=models.CASCADE, verbose_name='英雄属于的图书')
   # hbook = models.ForeignKey('BookInfo', on_delete=models.CASCADE, verbose_name='英雄属于的图书')
    hname = models.CharField(max_length=20, verbose_name='人名')
    hgender = models.SmallIntegerField(choices=GENDER_CHOICES, default=0, verbose_name='性别')
    hcomment = models.CharField(max_length=200, null=True, verbose_name='描述信息')
    is_delete = models.BooleanField(default=False, verbose_name='逻辑删除')

    class Meta:
        db_table = 'tb_heros'

    def __str__(self):
        return self.hname
```

> 2.进行数据迁移
>
> ```shell
> python manage.py makemigrations
> python manage.py migrate
> ```

3. 添加测试数据 到数据库

```SQL
mysql -uroot -pmysql
use django_demo;

insert into tb_books(btitle,bpub_date,bread,bcomment,is_delete) values
('射雕英雄传','1980-5-1',12,34,0),
('天龙八部','1986-7-24',36,40,0),
('笑傲江湖','1995-12-24',20,80,0),
('雪山飞狐','1987-11-11',58,24,0);
```

```SQL
insert into tb_heros(hname,hgender,hbook_id,hcomment,is_delete) values
('郭靖',1,1,'降龙十八掌',0),
('黄蓉',0,1,'打狗棍法',0),
('黄药师',1,1,'弹指神通',0),
('欧阳锋',1,1,'蛤蟆功',0),
('梅超风',0,1,'九阴白骨爪',0),
('乔峰',1,2,'降龙十八掌',0),
('段誉',1,2,'六脉神剑',0),
('虚竹',1,2,'天山六阳掌',0),
('王语嫣',0,2,'神仙姐姐',0),
('令狐冲',1,3,'独孤九剑',0),
('任盈盈',0,3,'弹琴',0),
('岳不群',1,3,'华山剑法',0),
('东方不败',0,3,'葵花宝典',0),
('胡斐',1,4,'胡家刀法',0),
('苗若兰',0,4,'黄衣',0),
('程灵素',0,4,'医术',0),
('袁紫衣',0,4,'六合拳',0);
```

# 2.CRUD

### 1.基本操作 crud

#### 增加

```python
# 1.save()
        book = BookInfo()
        book.btitle = '颈椎病修复术'
        book.bpub_date = '2008-01-01'
        book.save()
```

```python
 # 2.create()
        BookInfo.objects.create(
            btitle='腰椎病修复术',
            bpub_date = '2020-01-01'
        )
```

```python
# 关联增加
# 增加英雄---关联图书
hero = HeroInfo()
hero.hname = 'xxx'
hero.hbook_id = 1
hero.save()

book = BookInfo.objects.get(id=1)
HeroInfo.objects.create(hname='xxx', hbook=book)
```



### 修改

```shell
# save()
book = BookInfo.objects.get(id="值")
book.btitle = '新值'
book.save()
```

```shell
# update()
BookInfo.objects.filter(id="值").update(属性名字="新值")
```

### 删除

```python
book = BookInfo.objects.get(id="值")
book.delete()
```

```python
BookInfo.objects.filter(id=5).delete()
```

### 基本查询

```shell
# 只能返回一个数据对象  get() --如果不存在--报错--DoesNotExist
# 返回查询集querySet  filter() 
# 取反  querySet     exclude() 
# 取所有 						all()
# 统计个数 					 count()
```



### 过滤查询

```python
# BookInfo.objects.filter(属性名字__运算符=值)
# 查询编号为1的图书。(id=1) -- (id__exact=1)
# 查询书名包含'传'的图书。(btitle__contains='传')
# 查询书名以'部'结尾的图书(btitle__endswith='部')
# 查询书名不为空的图书。(btitle__isnull=False)
# 查询编号为1或3或5的图书 (id__in=[1,3,5])
# 查询编号大于3的图书 gt lt gte lte (id__gt=3)

# 查询编号不等于3的图书 exclude(id=3)
# 查询1980年发表的图书 (bpub_date__year=1980)
# 查询1980年12月1日后发表的图书。 (bpub_date__gt='1980-12-01')
```

### 过滤查询

```python
# F 对象 -- 多属性(字段)对比
from django.db.models import F
# 查询阅读量大于等于评论量的图书。
BookInfo.objects.filter(bread__gte = F('bcomment'))
# 查询阅读量大于2倍评论量的图书。
BookInfo.objects.filter(bread__gt = F('bcomment') * 2)
```

```python
# Q 对象 -- 多条件---逻辑与 逻辑或 逻辑非
from django.db.models import Q

# 查询阅读量大于20，并且编号小于3的图书  &
BookInfo.objects.filter(bread__gt=20, id__lt = 3)  # 默认多条件 就是逻辑与
BookInfo.objects.filter(Q(bread__gt=20) & Q(id__lt = 3))

# 查询阅读量大于20，或编号小于3的图书    |
BookInfo.objects.filter(Q(bread__gt=20) | Q(id__lt = 3))

# 查询阅读量不等于3的图书--- ~
BookInfo.objects.exclude(id=3)
BookInfo.objects.filter(~Q(id=3))
```

###  聚合查询 Avg Sum Max Min Count === aggregate()

```python
from django.db.models import Avg,Sum,Max,Min,Count

# 查询 所有图书的平均阅读量
BookInfo.objects.aggregate(Avg('bread'))

BookInfo.objects.count()
BookInfo.objects.aggregate(Count('字段名字'))
```

### 排序 order_by

```python
BookInfo.objects.order_by('id')
BookInfo.objects.all().order_by('-id')
```

###  关联查询

```python
多表查询

1张表 

图书表——英雄表
1:n(外)

# 查询 Id=3这本书的所有英雄
book = BookInfo.objects.get(id=3)
book.heroinfo_set.all()

# 查询英雄 属于哪本书
n:1
n.外键属性
hero = HeroInfo.objects.get(id=1)
hero.hbook
```

```python
# 扩展 1:n的另外一种写法 ---orm 和 heroinfo_set 只能存一--不能共存
1. 修改 HeroInfo的模型类--hbook 字段的参数--添加一个 related_name = 'abc'
# 查询 Id=3这本书的所有英雄
book = BookInfo.objects.get(id=3)
book.abc.all()

```

### 查询集的优势

```python
# querySet--filter() all() exclude() order_by() 
1.惰性执行--懒加载
2.缓存
切片---数字不能写负数
querset[0:2]
```

# Template

###  1.配置 django模板

```python
# 1.在 项目根目录--创建一个文件夹--templates
# 2. settings.py--TEMPLATES -- DIRS
# 配置模板
TEMPLATES = [
  {
      'BACKEND': 'django.template.backends.django.DjangoTemplates',
      #指定模板文件目录的路径
      'DIRS': [os.path.join(BASE_DIR, 'templates')],
      'APP_DIRS': True,
      'OPTIONS': {
          'context_processors': [
              'django.template.context_processors.debug',
              'django.template.context_processors.request',
              'django.contrib.auth.context_processors.auth',
              'django.contrib.messages.context_processors.messages',
          ],
      },
  },
]
```



###  2.使用django模板

```python
# 1.templates--创建前端文件 index.html
# 2.后台--views.py --def get():  
		return render(request, 'index.html', {'username':'张三'})
# 3.index.html --- {{ username }}
```



###  3. 小案例 --渲染数据库中所有的图书信息

```python
def get(request):
	 # 1. 查询数据库中所有的数据
    books = BookInfo.objects.all()
    
    context = {'books': books}
	 # 2. 将数据 给了 前端 模板文件
   return render(request, 'index.html', context)
	 
# 3.渲染 {% for i in books %}   <li> {{ i }} </li>  {% endfor %}
```









