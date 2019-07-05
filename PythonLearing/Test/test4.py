# test4 2019/7/3  函数

# # 函数内定义的变量，函数外不能使用
# def my_add(a,b):
#     ret = a + b
#     print('a + b=',ret)
#
# my_add(17,48)  # 位置参数
# my_add(a = 46,b = 45)  # 关键字参数

# 下面的数字是实参，上面的a，b是形参

# def my_add(a,b):
#     ret = a + b
#     return ret
#
#
# # 保存返回结果
# ret = my_add(122,143)
# # 进行下一步计算
# final_ret= ret + 23
# print(final_ret)

# 使用调试模式
# 1.先加断点
# 2.启动调试模式
# None表示什么都没有，也没有类型
# print和return的区别
# print只是一个函数，只是一个功能，return是一个语句，和def if类似
# print会将数据打印到屏幕上，return会将数据返回到程序中，给参数调用者


"""
1.1 函数的作用
    常用的功能写成函数的形式，可以在任何地方调用
1.2 函数定义的语法格式
    def 函数名 （a，b，c）：
        函数体

        return

1.3 函数调用的语法格式  函数名（10，20，30）

"""


# 编写一个函数用于计算从start开始到end结束之间所有的数字的累加和

# def all_adds(start,end):
#
#     # 判断start end是都是数字
#
#     if not my_type:
#         print('start 应该是一个数字！')
#         return None
#
#     i = start
#     s = 0
#     while i <= end:
#         s += i
#         i += 1
#
#     return s
#
# ret = all_adds(1,100)
# print('ret:',ret)

# # 编写一个函数根据传入的运算符，进行相应的 加减乘除 运算
#
# def my_caculator(left,right,operator):
#     a = left
#     b = right
#
#     if operator == '+':
#         ret = a + b
#     elif operator == '-':
#         ret = a - b
#     elif operator == '*':
#         ret = a * b
#     elif operator == '/':
#         ret = a / b
#     else:
#         print('输入的运算符有误！')
#         ret = None
#
#     return ret
#
# ret = my_caculator(10,20,'+')
# print('set:',ret)  # 位置参数
# ret = my_caculator(left=10,right=20,operator='*')  # 关键字参数
# print('set:',ret)
# ret = my_caculator(10,20,'@')
# print('set:',ret)

# 问题是：调用函数是即传递位置参数，又传递关键字参数，此时需要注意：
# 位置参数一定在关键字参数的前面

# return 关键字：
# 1.当函数执行到return的时候，就会马上终止执行
# 2.函数里面可以出现多个return，但是只会执行一个return
# 3.return后面可以不跟值，相当于return None