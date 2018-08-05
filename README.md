#
通过 Tools -> Run manage.py Task创建app：
输入 startapp message ,创建了message并存放在了项目同级目录。
新建log、media、static目录，并新建apps目录，
项目大了过后app过多的问题：
将message放入apps，并右键app文件夹设置为sourcce root，解决开
发环境下的环境变量问题，terminal运行环境的环境变量问题在setting中加入如下命令：
import sys
sys.path.insert(0,os.path.join(BASE_DIR,'apps'))（除了manage中，由于manage中还未载入setting
