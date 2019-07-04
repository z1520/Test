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


# # 猜拳游戏
# # 导入随机数
# import random
#
# while True:
#     # 获取用户的拳头
#     user_quan = int(input('请输入：石头（0）剪刀（1）布（2）'))
#     if user_quan == 3:
#         print('退出游戏！')
#         break
#     # 获取系统的拳头
#     computer_quan = random.randint(0,2)
#
#     # 判断胜负
#     # 用户赢的情况
#     if (user_quan == 0 and computer_quan == 1) or \
#         (user_quan == 1 and computer_quan == 2) or \
#         (user_quan == 2 and computer_quan == 0):
#         print('您赢了！')
#     elif user_quan == computer_quan:
#         print('平局！')
#     else:
#         print('您输了！')


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


# # 水仙花数  （未执行完）
# # import
# # 表示水仙花数每个位上的数字
# for n in range(100,999):
# # 给出n的三个数字
#     a = n // 100
#     b = n //10 % 10
#     c = n % 10
# # 写出求和公式
# my_sum = int(a ** 3 + b ** 3 + c ** 3)
# while range(100,999,):
#     if n != my_sum:
#         continue
#
# print('水仙花数是：d%',n)

# # 完美数:除开自身以外的约数的和等于其自身
#
# for i in range(1,1000):
#     s = 0
#     for a in range(1,i):
#         if i%a == 0:
#             s += a
#     if s == i:
#         print(i)

# Fibonacci斐波那契数列，又称黄金分割。比如 1 1 2 3 5 8 13...









#  简易版的员工管理系统
# 1 接受用户输入
# 2.1 展示所有员工信息
# 2.2 新增一个员工信息
# 2.3 修改一个员工信息
# 2.4 删除一个员工信息
# 2.5 退出员工管理系统


# print('欢迎使用【员工管理系统v1.0】')
#
# while True:
#     # 展示系统菜单
#     print('*' * 10 + '操作菜单' + '*' * 10)
#     print('1. 展示所有员工信息')
#     print('2. 新增一个员工信息')
#     print('3. 修改一个员工信息')
#     print('4. 删除一个员工信息')
#     print('5. 退出员工管理系统')
#     print('*' * 26)
#     # 保存用户操作
#     user_operration = int(input('请输入您的操作：'))
#     if user_operration == 1:
#         print('姓名\t年龄\t性别\t')
#         print('小米\t34\t男\t')
#     elif user_operration == 2:
#         name = input('请输入姓名：')
#         age = input('请输入年龄：')
#         rex = input('请输入性别：')
#         print('新员工 %s 添加到系统成功！' % name)
#     elif user_operration == 3:
#         name = input('请输入你要修改的员工：')
#         print('员工 %s 的信息修改成功！' % name)
#     elif user_operration == 4:
#         name = input('请输入你要删除的员工姓名：')
#         print('员工 %s 已被成功删除！' % name)
#
#     elif user_operration == 5:
#         print('退出员工管理系统成功！')
#         print('欢迎再次使用！')
#         break
#     else:
#         print('输出有误！')


