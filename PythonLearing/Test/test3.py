# test3 2019/6/29

# # 输入两个数，计算出两个数之和
# left_num = int(input('请输入第一个数:'))
# right_num = int(input('请输入第二个数:'))
# # 打印两个数的类型
# # print(type(left_num),type(right_num))
# # 转换两个数的类型
# left_num_int = int(left_num)
# right_num_int = int(right_num)
# # 进行加法运算
# result = left_num_int + right_num_int
# print(result)
# # 输出结果
# print('%d + %d 的结果是 %d' % (left_num_int,right_num_int,result))

# BUG
"""
bug会导致系统崩溃，停止运行
bug会导致程序执行结果不是预期
"""


# # # 猜拳游戏
# # # 导入随机数
# # import random
# #
# # 获取用户的拳头
# user_quan = int(input('请输入：石头（0）剪刀（1）布（2）'))
# # 获取系统的拳头
# computer_quan = random.randint(0,2)
# # 判断胜负
# # 用户赢的情况
# if (user_quan == 0 and computer_quan == 1) or \
#     (user_quan == 1 and computer_quan == 2) or \
#     (user_quan == 2 and computer_quan == 0):
#     print('您赢了！')
# elif user_quan == computer_quan:
#     print('平局！')
# else:
#     print('您输了！')


# 重复的代码越多，后期维护的工作量就越大，成本越高
# 复用（重复使用）
# 如果条件永远被满足，那么程序会一直被执行下去
# while 循环场景，有些代码需要循环执行

# 打印1-100的数字
# i = 1
# while i <= 100:
#     print(i)
#
#     i += 1
# print('end')

# 打印1-100之间的偶数
# i = 1
# while i <= 100:
#     if i%2 == 0:
#         print(i)
#     i = i + 1


# 计算1-100之间所有数的累加和
# i= 1
# # 所以数的和
# totle = 0
# while i <= 100:
#     totle = totle + i
#     i += 1
# print('总和:' ,totle)

#  计算1-100之间的奇数和
# i = 1
# totle = 0
# while i <= 100:
#     if i %2 == 1:
#         print(i)
#         totle = totle + i
#     else:
#         totle = totle
#     i = i + 1
# print('总和：',totle)


# 计算1-100之间的所有数的累加和。50不能累加
# index = 1
# my_sun = 0
# while index <= 100:
#     if index == 50:
#         index += 1
#         continue
#     my_sun += index
#     index += 1
#
# print('最终结果：',my_sun)

# 当执行到continue，后面的代码不再执行，直接回到while后面的条件判重新断跳过本次循环，不是退出循环
# 只有在循环中才能写continue


# break 退出循环
# print('循环开始...')
# i = 0
# while i <= 100:
#
#     if i > 50:
#         break
#     print(i)
#     i += 1

# break 执行，后面的代码不再执行，并且马上终止循环


# 水仙花数  （未执行完）
# import
# 表示水仙花数每个位上的数字
for n in range(100,999,1):
# 给出n的三个数字
    a = n // 100
    b = n //10 % 10
    c = n % 10
# 写出求和公式
my_sum = int(a ** 3 + b ** 3 + c ** 3)
while range(100,999,):
    if n != my_sum:
        continue
    else:
       print('水仙花数是：',n)







