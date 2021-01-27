# # num = input("请输入你的名字")
# # gen = input("请输入你的年龄")
# # ox = input("请输入你的性别")
# # print('''************************
# # 姓名：{}
# # 年龄：{}
# # 性别：{}
# # ************************
# # '''.format(num,gen,ox))
# # str1='python hello aaa 123123aabb'
# # print(str1[0:7:1])# =python
# # print('oa'in str1)# =False
# # print('ab'in str1)# =True
# # print(str1.replace("python","lemon")) #=lemon hello aaa 123123aabb
# # print(str1.index("a"))
# # C= [1,1.3,"子琳",True,[1,2,3,4]]
# # C.append("子琳")
# # print(C) #=[1, 1.3, '子琳', True, [1, 2, 3, 4], '子琳']
# # # print(len(C))
# # tuple1=(1, 1.3, '子琳', True, [1, 2, 3, 4], '子琳')
# # C = list(tuple1)  #把元组转换为列表
# # print(C)
# # dict1 = {"name":"claflin","height":"171","weight":"120"}
# # dict1.update({"city":"beijing","hobby":"baskeball","gender":"23"})
# # # print(dict1)
# # list2 = [1,1,2,31,33,21,2,1]
# # set1 = set(list2)   #将列表转化为集合，去重
# # print(set1)
# # list2 = list(set1)   #将去重完的集合，转化为列表
# # print(list2)
# # money = int(input("请输入你的金额："))
# # if money >= 500 :
# #     print("买IPhone")
# # elif money >= 200 :
# #     print("买西瓜")
# # elif money >= 50 :
# #     print("买栗子")
# # else :
# #     print("滚回去赚钱")
# # list1 = ['哈哈','嘻嘻','呵呵','嘿嘿','啦啦','波波','嘛嘛']
# # # # for name in list1 :
# # # #     if name == "嘿嘿" :
# # # #         continue  #跳出本次循环
# # # #     print(name)
# # for i in range(1,8,2):
# #     print(i)
# def good_job (salary,bonus,subsidy,*args,**kwargs):    #定义---函数名=== 函数的参数---形参--变量替代
#     sum1 = salary+bonus+subsidy   #sum1 实现功能
#     for i in args:
#         sum1 += i
#     for j in kwargs:
#         sum1 += kwargs[j]
#     return sum1 , salary  #定义多个返回值，用逗号隔开
# # result = good_job(2000,800,1000)
# c = "啦啦啦",22,104.5,"嘿嘿"
# d = list(c)
# print(d)
# c = {22,"小黑",223}
# if len(c)>5:
#     print("true")
# else:
#     print("Flase")
# c = 1,3,2,4
# d = range(c)
#
# dict_1={"class_id":45,'num':20}
# if dict_1['num']>5:
#     print("班上人数为{}".format(dict_1['num']))
# else:
#     print("班上人数不足5人")
# #手动
# list1=['放放图','其母','荷花鱼','焕蓝','claflin','康康']
# c = {"name":"放放图","xingbie":"男","age":11,"city":"beijing"}
# d = {"name":"其母","xingbie":"女","age":13,"city":"quanzhou"}
# e = {"name":"荷花鱼","xingbie":"男","age":10,"city":"beijing"}
# f = {"name":"焕蓝","xingbie":"男","age":18,"city":"shanghai"}
# g = {"name":"claflin","xingbie":"女","age":12,"city":"beijing"}
# h = {"name":"康康","xingbie":"男","age":28,"city":"beijing"}
# list2 = ([c,d,e,f,g,h])
# print(list2)
# #自动
# list1 = ['放放图','其母','荷花鱼','焕蓝','claflin','康康']
# list2 = [] #空列表，生成的字典放入这个列表里
# list3 = ["男","女","女","男","男","男",]
# list4 = ["19","20","22","88","23","22"]
# list5 = ["beijing","shanghai","beijing","quanzhou","jinjiang","shanghai"]
# for w in range(6):
#     dict1 = dict(name=list1[w],sex=list3[w],age=list4[w],city=list5[w])
#     list2.append(dict1)
# # print(list2)
# c = [1,2,3,1,2,3,4]
# for i in range(6):
#     sum += i
# print(i)
# #浏览器常用操作：1、打开一个网址
# drive.get("http://8.129.91.152:8765/")
# #2、浏览器最大化

# #3、打开新的页面 延迟
# time.sleep(3)   #等待 默认为秒
# drive.get("https://baidu.com/")
# #4、向前 退后 刷新页面
# time.sleep(3)
# drive.back() #退回上一个页面
# time.sleep(3)
# drive.forward()  #前进到下一个页面
# time.sleep(3)
# drive.refresh()   #刷新页面
# #5、退出
# drive.quit()  #关闭驱动   会话会关闭
# #drive.close()   #关闭当前的窗口，但不会退出会话
# # #非常规操作====怎么实现？ ====元素定位：找标签 -- 了解 前端页面
# from selenium import webdriver  #从selenium工具导入webdriver库
# import time
# drive = webdriver.Chrome()   #选择chrome浏览器，初始化driver=== 可以浏览器进行沟通，建立会话
# drive.implicitly_wait(10)#  隐式等待，默认等待10s  ===最多等10秒，提前出现了，不继续等待
# # # #1、打开一个网址
# drive.get("http://erp.lemfix.com/login.html")
# #2、浏览器最大化
# drive.maximize_window()
# #输入用户名
# drive.find_element_by_id("username").send_keys("test123")   #找到了有username这个id的元素---点击、输入内容
# #输入密码
# drive.find_element_by_id("password").send_keys("123456")
# #点击登录
# drive.find_element_by_id("btnSubmit").click()
# #点击零售出库
# drive.find_element_by_xpath("//a[@title='零售出库']").click()
# #定位iframe，获取id
# P_ID = drive.find_element_by_xpath("//div[text()='零售出库']/..").get_attribute("id")    #找到元素定位，获取id
# J_ID = P_ID+"-frame"#找到元素定位，获取id
# #通过下标值来切换iframe
# drive.switch_to.frame(1)
# #搜索单据编号710
# drive.find_element_by_id("searchNumber").send_keys("710")
# drive.find_element_by_id("searchBtn").click()
# time.sleep(3)    #要睡一下否则页面刷新不出来
# #验证单据编号与搜索是否一致
# num = drive.find_element_by_xpath("//tr [@id='datagrid-row-r1-2-0']//td [@field='number']//div").text
# if "710" in num:
#     print("搜索结果正确")
# else:
#     print("搜索结果错误")
import time
def login_in(username,password,drive) :    #形参  参数化 提高代码复用率
    drive.find_element_by_id("username").send_keys(username)
    drive.find_element_by_id("password").send_keys(password)
    drive.find_element_by_id("btnSubmit").click()
def open_url(url,drive):  #打开网页
    drive.get(url)
    drive.maximize_window()
def search(url, drive,username,password,key):
    open_url(url, drive)
    login_in(username,password,drive)
    drive.find_element_by_xpath("//a[@title='零售出库']").click()
    P_ID = drive.find_element_by_xpath("//div[text()='零售出库']/..").get_attribute("id")    #找到元素定位，获取id
    J_ID = P_ID+"-frame"
    drive.switch_to.frame(1)
    #搜索单据编号710
    drive.find_element_by_id("searchNumber").send_keys(key)
    drive.find_element_by_id("searchBtn").click()
    time.sleep(3)    #要睡一下否则页面刷新不出来
    #验证单据编号与搜索是否一致
    num = drive.find_element_by_xpath("//tr [@id='datagrid-row-r1-2-0']//td [@field='number']//div").text
#给别人使用的变量-----定义成返回值
    return num