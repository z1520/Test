# test2 2019/6/26  变量和运算符

"""
变量的作用：
临时存储程序运行中所需要的数据
赋值==定义变量

变量命名的规则：
字母，数字或者下划线组成，数字不能开头
pathon中区分大小写
一般是小写字母加下划线组成
不能和关键字或者已有变量名冲突
命名要有意义，能提升代码的可读性

在现实生活中，有很多数据类型，类型约定了数据之间的计算规则
integer 整数类型    float 小数类型（浮点型） string 文本（字符串类型） bool 布尔类型（变量只有true和false）
可以用type函数查看变量类型
复制运算符‘=’，先看右边的，再看左边

字符串之间支持加法运算，不支持减法运算
str1 = 'hello'
str2 = 'world'
new_str = str1 + str2
print(new_str)  # 不能加引号，否则只会输出new_str这个变量名
数字和字符串之间支持乘法运算

输入和输出，简称i/o  intput和output
标准I/O 标准的输入和输出，从键盘读，往屏幕写
文件I/O 从文件读，往文件写
网络I/O

函数中的逗号用来隔开多个变量    \n表示换行  end=''表示不换行
"""

# 华氏温度转换为摄氏温度
from math import pi

h_temp = float(input('华氏温度='))
s_temp = float((h_temp-32)*5/9)  # 摄氏温度
print(round(s_temp,2))  # round函数返回小数点四舍五入的n个数字

# 输入圆的半径计算周长和面积
import math
r = float(input('园的半径r='))
s = float(round(math.pi*(r**2)))
c = float(round(math.pi*2*r))
print()  # 园的面积
result = '园的面积为%d,圆的周长为%d.'%(s,c)  # 圆的面积和周长
print(result)


#输入年份判断是否是闰年
year = int(input('请输入年份：'))
number1 = year%4
number2 = year%100
number3 = year%400
print(number1 , number2 , number3)
if number1 == 0 and number2 != 0 :  # 当年份能被4整除且不能被100整除时
    print("闰年")
else:
    if number3 == 0:  # 当年份能被400整除
        print("闰年")
    else:
        print("非闰年")



#  2019/6/27 输入和输出
"""
占位符：占位，位置上数据的类型
%s string
%d digit(数字)
%f float
%% 输出百分号

\n表示换行  end=''表示不换行
print('aaa',end='#')
print('bbb',end='#')
print('ccc',end='#')

格式化输出
name = 'z1520'
age = 3
salary = 0.1
print()
my_ format = '我的名字是d%，我的年龄是d%,我的工资是d%.' % (name,age,salary)
print(my_format)

"""
name = 'z1520'
age = 3
salary = 0.1
print()
my_format = '我的名字是%s，我的年龄是%d,我的工资是%.2f.' % (name,age,salary)
print(my_format)
