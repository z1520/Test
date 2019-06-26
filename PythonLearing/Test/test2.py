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
"""

# 华氏温度转换为摄氏温度