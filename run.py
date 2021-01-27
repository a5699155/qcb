from python_class import lesson_01   #导入函数
from test_data import test_date   #导入数据
from selenium import webdriver  #从selenium工具导入webdriver库
import time
drive = webdriver.Chrome()   #选择chrome浏览器，初始化driver=== 可以浏览器进行沟通，建立会话
drive.implicitly_wait(10)#  隐式等待，默认等待10s  ===最多等10秒，提前出现了，不继续等待
#取值    1、先参数取出来   2、传参到函数调用里
url = test_date.url["url"]   #取值url
use = test_date.login_in["username"]   #取值用户名
pwd = test_date.login_in["password"]   #取值密码
key = test_date.key["key"]    #取值搜索结果
print(url,use,pwd,key)
#调用函数   传参
#给函数定义了一个返回值----调用的时候用一个变量接收返回值：
result = lesson_01.search(drive=drive,url=url,username=use,password=pwd,key=key)

if key in result:
    print("搜索结果正确")
else:
    print("搜索结果错误")