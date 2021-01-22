#  学习方法:

##1.以后 所有的课件和素材的压缩文件--拖拽 ubuntu --再解压 (课件添加到浏览器的书签)

##2. 有BUG 先瞄瞄经验值表--->问组员--->老师--->度娘

##3.每天课前预习和当天单词熟练

# 晚自习必做事情

# 1.注册 http://www.github.com
# 2.注册 http://www.gitee.com

### 3.目标反馈

### 4. 当天小结笔记



# 1.NoSQL

### 概述

* 泛指非关系型数据库 和 关系型数据库取反的
* Key-Value---形式 ===>dict  javascript对象
* 学习成本高一些---一个数据库一种API(接口-语法)

### 使用场景:

* 1.购物车,浏览记录
* 2.缓存
* 3.大数据,数据采集(爬虫):旅游类的公司----携程,途牛,飞猪,马蜂窝, 驴妈妈,去哪网,同程,艺龙

######   

# 2.redis数据库

######      1.特点:

* 1.K-V形式的数据库
* 2.底层C语言---内存型数据库亦可持久化----

######      2.作用场景:

* 1.购物车,浏览记录
* 2.缓存
* 3.大数据,数据采集(爬虫):旅游类的公司----携程,途牛,飞猪,马蜂窝, 驴妈妈,去哪网,同程,艺龙
* 4.数据类型:5种--string-hash-list-set-zset

# 3.Redis安装  ubuntu

######  1.去官网 下载 安装包

###### 2.解压 tar 

###### 3.移动到 /usr/local

###### 4.本地安装  sudo make install

###### 5.将配置 文件---移动到 /etc/redis/



# 4.Redis 配置文件

* 1.daemon yes -- 是否以后台启动  redis 服务 --yes  允许后台启动
* 2.bind --改IP 的
* 3.port --改 端口号 6379
* 4.databases  -- 16个 -- 0-15
* 
* 4.slaveof --主从配置
* 5.pidfile -- 进程id文件
* 6.logfile  -- 日志文件
* 8.savle-read-only  --从端只读
* 9.protected-mode --- 是否允许远程链接--默认是yes(不允许) --no(允许远程)

# 5.Redis启动命令

* 1.服务端
  
  * redis-server
  * 默认启动的 redis服务 是占主进程 
  
* 2.客户端
  
  * redis-cli
  
  
  
* 3.第二种方式 以配置文件启动:
  
  * 以配置文件启动
    * redis-server /etc/redis/redis.conf
    * redis-cli
  * 查看真实IP: ifconfig
  * 查看进程id: ps aux|grep redis
  * 杀进程: kill -9 进程id值
  * redis-cli -h 真实IP(前提条件--配置文件 添加真实IP bind)



# 6.数据操作: string--hash--list--set-zset

config set stop-writes-on-bgsave-error no

## 1.string -CRUD

* 增  set k v
  * mset
* 删  del k
* 改  set k v
* 查 get k
* 追加 append k v
* 设置过期 setex k seconds v
* 递增: 
  * set A 1
  * incr A 每次只增加1
  * incrby A 100
* 递减:
  * set A 100
  * decr A每次只减少1
  * decrby A 20



## 2.键的操作-KEY

* 1.查  keys  *
* 2.删 del key
* 3.存在 exists key
* 4.键的类型 type key
* 5.设置key过期时间 expire key time
* 6.查看过期时间 ttl key
* 7.清空当前数据库的数据  flushdb
* 8.清空所有数据库数据 flushall
* 9.切换select index 

### 3.hash类型---存储对象的--万物皆对象-- cat对象--color:黑---age:12--gender:true

```javascript
hash:{
  	person :{
               name: '川建国',
               age:"74",
            }
	}
```



- 增  hset k 属性  v
- 删  hdel k 属性
  - del k 删除整个对象
- 改 hset k 属性 新v
- 查  hget k 属性
- 获取所有值: hvals k
- 获取所有属性:hkeys k
- 获取所有的属性和值:hgetall k

### 4.list--列表

* 队列顺序: FILO 先进后出 
  * ​		  FIFO 先进先出

- 增  
  - 左插入 lpush k v v1 v2
  - 右插入rpush k v v1 v2
  - 指定元素插入: linsert k before/after old_value new_value
- 删 lrem k count v
  - lrem k 正数 v
  - lrem k 负数 v
  - lrem k  0  v
- 改 lset k index new_v
- 查: lrange k start_index stop_index
- 切片: ltrim k start_index stop_index

### 4.set:无序--不重复

- 增 sadd k v
- 删 srem k v
- 查 smembers k

## 5.zset:有序(score --得分,权重)--不重复

- 增 zadd k score v score1 v2
- 删 zrem k v
  - 以权重范围删除: zremrangebyscore k min max
- 查 zrange k start_index stop_index
  - 以权重范围查询:zrangebyscore k min_score max_score
- 根据元素获取权重: zscore k v

#  7.redis和python交互

* 1.mysql和Python 交互流程:装包---1.导包  2.创建链接    3.执行CRUD
* 2.redis和和Python 交互流程:
  * 装包 --sudo pip3 install redis
  * 1.导包  import redis
  *  2.创建链接  redis.StrictRedis( )
  * 3.执行CRUD--del==delete
* 千万注意: 取出的数据类型 是 bytes类型---decode()

| 类型 | 增   | 删   | 改   | 查   | 其他 |
| ---- | ---- | ---- | ---- | ---- | ---- |
|      |      |      |      |      |      |
|      |      |      |      |      |      |
|      |      |      |      |      |      |
|      |      |      |      |      |      |
|      |      |      |      |      |      |





# 1.以下nosql 描述正确的是: 多选

A. 不能使用SQL语句

B.一定是非关系型数据库

C.数据之间没有关联

D.不支持事务

# 2.以下不是redis的优点的是: 单选

A. 内存型

B.底层C#实现

C.KV 形式

D.持久化数据

# 3.以下是绑定IP的配置项是单选:

A.databases 16

B.bind

C.daemon yes

D.logfile



# Git

### 作用:源代码管理器

* 1.多人协同开发 合并代码  自动合并
* 2.发布代码---记录版本, 备份代码 

### 分布式:

* 1.一个人盖房子 ---1年
* 包工头--30个人 --一个月

### Git 区域

* 1.工作区--写代码地方
* 2.暂存区--临时 存储
* 3.本地仓库区-- 记录版本
* 4.远程仓库---合并代码

### Git 本地操作--单人

* 1.新建一个本地仓库
  * git init
* 2.配置 用户名 和 邮箱
  * git config user.name xxx
  * git config user.email xx@qq.com
* 3.写代码--随意写-- touch login.py
* 4.从工作区 提交到 ---暂存区 git add login.py
* 5.从暂存区 提交到---本地仓库区 git commit -m '提交的功能描述'


























