# test6 2019/7/19

"""
读文件 - 读取整个文件 / 逐行读取 / 文件路径
写文件 - 覆盖写入 / 追加写入 / 文本文件 / 二进制文件
异常处理 - 异常机制的重要性 / try-except代码块 / else代码块 / finally代码块 / 内置异常类型 / 异常栈 / raise语句
数据持久化 - CSV文件概述 / csv模块的应用 / JSON数据格式 / json模块的应用

"""
# 读写文件是最常见的IO操作

# 文件打开分为两种：文本模式   二进制模式
"""
r:以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式
w:打开一个文件只用于写入，如果该文件已存在则将其覆盖。如果文件不存在，创建新文件
a:打开一个文件用于追加，如果该文件已存在，文件的指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有的内容之后，如果文件不存在，创建文件进行写入
rb:以二进制的格式打开一个文件用于只读。文件的指针将会放在文件的开头。这是默认模式
wb:以二进制的格式打开一个文件只用于写入，如果该文件已存在则将其覆盖，如果文件不存在，创建新文件
ab:以二进制格式打开一个文件用于追加。如果该文件存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后，如果文件不存在，创建新文件进行读写

"""
# 文件：文件的作用就是计算机存储数据
# 在python中，使用open函数，可以打开一个已经存在的文件，或者创建一个新文件，使用close函数来关闭一个文件

# # 打开文件
# fa = open('a.txt','w',encoding='UTF-8')
# my_content = 'hello world! 第一次写入文件！\n'
# fa.write(my_content)
# # print(my_content)
# # 关闭文件
# fa.close()
#
# # 读取文件数据
# fb = open('b.txt','r',encoding='UTF-8')
# # read函数默认读取文件中的所有数据
# my_content = fb.read()
# # print(my_content)
# fb.close()

# 打开文件用的文本模式，会进行换算符的转换
# 打开文件用的是二进制模式的话，不会进行换算符转换
# 文件本质上都是以二进制的方式存储在磁盘上

# 文件打开模式
# w  r  a

def test01():
    """读的方式打开文件"""

    f = open('a.txt','r',encoding='UTF-8')
    content = f.read()
    print(content)
    f.close()

# test01()

def test02():
    """写文件"""
    # w 模式默认十会覆盖文件中的数据的
    # w 模式如果发现文件不存在，则会新建文件

    f = open('a.txt','w',encoding='UTF-8')
    f.write('hahahahha')
    f.close()

# test02()

def test03():

    f = open('a.txt','a')
    f.write('\nhello python')
    f.close()

# test03()

# 写文件

def test04():
    """1.write函数用法"""
    # write函数一次写一行
    f = open('a.txt','w')
    lines = ['aaa\n','bbb\n','ccc\n']
    # writelines一次可以写入多行，参数是一个列表，列表的每一个元素都是一行数据
    f.writelines(lines)
    f.close()

# test04()

def test05():
    """2.读操作"""

    f = open('a.txt','r',encoding='UTF-8')
    # read没有指定参数，则读取文件中的所有数据
    # read没有参数，则读取参数指定个数的数据
    content = f.read()
    f.close()

    print(content)

# test05()

def test06():
    """一次读取一行"""

    f = open('a.txt','r',encoding='UTF-8')
    content1 = f.readline()
    content2 = f.readline()

    print(content1)
    print(content2)
    f.close()

# test06()

def test07():
    """一次读取所有行"""
    f = open('a.txt', 'r', encoding='UTF-8')
    # content = f.readlines()
    # print(content)
    lines = f.readlines()
    for line in lines:

        if line[-1] == '\n':
            print(line[:-1])
        else:
            print(line)

    f.close()

# test07()

# 文件操作
import os

def file_rename():
    """文件重命名"""
    os.rename('清明雨上','清明雨上.txt')

def test08():
    """文件删除"""
    os.remove('c.txt')

# file_rename()
# test08()

# 路径问题：如果只写文件名，默认在当前目录修啊找文件，否则就会报错！

# 创建和删除目录
# os.mkdir('abc')  # 创建
# os.rmdir('abc')  # 删除


# 参考资料：https://www.runoob.com/python3/python3-errors-execptions.html
"""
1.概念引入：
错误：会引起程序的异常  错误是由于逻辑或者语法等导致一个程序无法正常执行的问题
异常：错误发生时的一种状态  当异常发生时，程序不会向下执行，而转去调用此函数的地方待处理错误并恢复正常状态
2.作用：
用作信号，通知上层调用者有错误产生需要处理
在程序调用层数较空时，想主函数传递错误信息需要层层return返回比较麻烦，用异常处理机制就相对简单的多，代码量大大减少

"""


# 处理异常的语句
# try-except 尝试捕获异常（就受异常通知），将程序转为正常状态并继续执行
# try-finally
# finally语子句不可以省略，一定不存在except子句
# 通常用try-finally 语句来做触发异常时必须要处理的事情，无论异常是否发生，finally语句都会执行
# expect 其他异常处理语句
# else 未发生错误执行的语句，发生错误不执行
# finally 最终语句，不管正常或者异常都一定会执行

# try:
#     sun = 1 + '1'
#     f = open('我为什么是一个文件.txt')
#     print(f.read())
#     f.close()
# except OSError as reason:  # 其他异常处理语句
#     print('文件出错了！错误的原因是:' + str(reason))
# except TypeError as reason:  # 其他异常处理语句
#     print('文件出错了！错误的原因是:' + str(reason))

"""
raise 作用：1.触发一个异常，让程序进入异常状态  2.发送错误通知给调用者
语法：
raise 异常类型
或
raise 异常对象
或
raise  # 重新触发上一次异常
"""
# def make_except():
#     print('开始')
#     try:
#         raise ValueError  # 故意发送一个错误通知
#     except:
#         print('接收到异常通知，已处理转为正常状态')
#     print('调用结束')
#
# try:
#     make_except()
# except:
#     print('接收到异常通知，已处理转为正常状态')
# print('程序结束')

"""
# 异常类型：
1.AttributeError：访问对象属性时引发的异常，如属性不存在或不支持赋值等。
2.ImportError：导入模块出错引发的异常（ 无法引入模块或包；基本上是路径问题或名称错误）。
3.IndexError ：下标索引超出序列边界，比如当x只有三个元素，却试图访问x[5]
4.IndentationError：没使用正确缩进时引发的异常（ 语法错误（的子类） ；代码没有正确对齐）。
5.TypeError ：在运算或函数调用中，使用了不兼容的类型时引发的异常（传入对象类型与要求的不符合）。
6.KeyError ：试图访问字典里不存在的键
7.KeyboardInterrupt： Ctrl+C被按下
8.NameError ：尝试访问一个没有申明的变量
9.SyntaxError： Python代码非法，代码不能编译(个人认为这是语法错误，写错了）
10.UnboundLocalError ：试图访问一个还未被设置的局部变量，基本上是由于另有一个同名的全局变量，导致你以为正在访问它
11.ValueError ：传入一个调用者不期望的值，即使值的类型是正确的
12.IOError ：输入/输出异常；基本上是无法打开文件
13.EOFError：使用input()函数读文件时，遇到文件结束标志EOF时发生的异常。文件对象的read()和readline()方法遇到EOF时返回空子字符串，不会引发异常。
"""

# python中用于处理异常栈的模块是traceback模块，它提供了print_exception、format_exception等输出异常栈等常用的工具函数。


# CSV文件写入
# 结构化数据字典（dict）的写入方式
# import csv
#
# with open('data.csv','w',encoding='UTF-8') as file:
#     writer = csv.writer(file)
#     writer.writerow(['id','name','sex'])
#     writer.writerow(['01','张三','男'])
#     writer.writerow(['02','李四','女'])

# 首先还是先打开data.csv文件，通过csv.writer（）定义一个写入对象，通过writerow()函数传入每行的数据写即完成数据的写入
# 也可以通过修改列与列之间的分隔符，可以在csv.writer()函数中传入delimiter参数，通过定义参数分隔符来实现此功能
# import csv
#
# with open('data.csv','w',encoding='UTF-8') as file:
#     writer = csv.writer(file,delimiter ='$')
#     writer.writerow(['id','name','sex'])
#     writer.writerow(['01','张三','男'])
#     writer.writerow(['02','李四','女'])

# 当调用writerows()方法同时写入多行，此时的参数就需要为二位列表
# import csv
#
# with open('data.csv','w',encoding='UTF-8') as file:
#     writer = csv.writer(file)
#     writer.writerow(['id','name','sex'])
#     writer.writerows([['01','张三','男'],['02','李四','女'],['03','王五','男']])

# csv数据读取同样也是根据csv库来进行操作的
# import csv
#
# with open('data.csv','r',encoding='UTF-8') as file:
#     reader = csv.reader(file)
#     for row in reader:
#         if reader == '\n':
#             print(row[:-1])
#         else:
#             print(row)
# 构造Reader对象，通过遍历对象，输出每行内容，每行都是一个列表形式。因为csv文件中包含中文，所以指定的encoding是utf-8编码

#JSON(JavaScript Object Notation, JS 对象标记) 是一种轻量级(传输数据的一种格式)的数据交换格式。
# JSON的数据格式其实就是python里面的字典格式，里面可以包含方括号括起来的数组，也就是python里面的列表。
# 在python中，有专门处理json格式的模块—— json 和 picle模块
# Json 模块提供了四个方法：dumps、dump、loads、load
# pickle 模块也提供了四个功能：dumps、dump、loads、load

# json模块的使用其实很简单，对于绝大多数场合下，我们只需要使用下面四个方法就可以了：
#
# 方法                  功能
#
# json.dump(obj, fp)  将python数据类型转换并保存到json格式的文件内。
#
# json.dumps(obj)     将python数据类型转换为json格式的字符串。
#
# json.load(fp)       从json格式的文件中读取数据并转换为python的类型。
#
# json.loads(s)       将json格式的字符串转换为python的类型。


# # 1. dumps
# import json
#
# list_a = [1,2,8,3,4,5]
# f = open('a.txt','w',encoding='UTF-8')
# list_a = json.dumps(list_a)  # dumps 功能是; 将其他数据类型容器,数据以字符串的形式保存
# print(list_a,type(list_a))
# f.write(list_a)
# f.close()
#
# # 2. loads
# import json
#
# f = open('a.txt','r',encoding='UTF-8')
# files = f.read()
# files = json.loads(files)  # loads 将字符串包裹的类型还原原有的数据类型
# print(files,type(files))
# f.close()
#
# # 3. dump
# import json
#
# list_a = [1,5,9]
# f = open('a.txt','w',encoding='UTF-8')
# json.dump(list_a,f)  # dump 接收两个参数  数据 句柄
# f.close()
#
# # 4.load
# import json
#
# f = open('a.txt','r',encoding='UTF-8')
# con = json.load(f)  # load 接收 句柄
# f.close()
#
# print(con,type(con))




# import os
#
# def file_rename():
#     """文件重命名"""
#
#     os.rename('test07.py','test7.py')
#
# file_rename()
