###
通过 Tools -> Run manage.py Task创建app：
输入 startapp message ,创建了message并存放在了项目同级目录。
新建log、media、static目录，并新建apps目录，
项目大了过后app过多的问题：
将message放入apps，并右键app文件夹设置为sourcce root，解决开
发环境下的环境变量问题，terminal运行环境的环境变量问题在setting中加入如下命令：
import sys
sys.path.insert(0,os.path.join(BASE_DIR,'apps'))（除了manage中，由于manage中还未载入setting
数据库驱动采用pymysql
记得在setting中：import pymysql; pymysql.install_as_MySQLdb()

Tools 菜单下 Run manage.py Task:(创建数据表)
makemigrations
migrate
加入静态文件路径：(此处变量名曾经输错)
>STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]
##项目配置流程图
我们刚才是以倒序：

1.把html文件放进来
2.通过简单的url配置来访问html。
3.发现找不到页面，所以我们设置setting中DIRS
4.文件找到了又说找不到静态文件，我们设置了STATICFILES_DIRS
推荐新建一个项目再按照正向流程图来一遍
后面我们的工作会围绕从migration生成数据表往下的内容展开。
##增加数据表步骤：
1.model中增加类
2.setting中注册message app
3.运行 makemigrations message 生成可执行文件
4.运行 migrate message 执行文件生成数据表
#
debug 模式 f8 单步往下继续执行 断点
查看数据变化情况（filter 函数： 过滤器，取出满足条件的特定对象）
django的安全机制，post页面需要加入crsf验证    {% csrf_token %}

url 别名
在 urls.py 中设置 name属性，此时，在前端中调用就可采用action=“{{ url name }}”的方式，修改路由后不需要再更改前端中的值
Django 关于 templete的配置
