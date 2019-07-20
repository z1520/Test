# test5 2019/7/8  容器（符串，列表，元组，字典）

# 多种容器根据存储数据的特点，分为序列式容器和非序列式容器。
# 序列式容器中的元素存放时是连续性的，包括字符串，列表，元组
# 非序列式在存储元素时不是连续存放的，包括字典，集合

# my_str = 'abcd'
#
# my_str[0] = 'Q'
# print(my_str)

# 1. 字符串一旦定义不允许修改
# 2. 字符串容器中的元素都是字符类型的

# 遍历：不重复的饭访问容器中的每一个元素
# 索引支持整数索引，也支持负数索引
# my_str = 'hello'
# print(my_str[2])  # 2是索引  下标
# i = 0
# while i <5:
#     print(my_str[i],end='')
#     i = i+1

# my_str = 'hello'
#
# print()
# for v in my_str:
#     print(v,end=' ')
6

# poetry = '有朋自远方来，不亦说乎.说'

# # replace并不会把原来的字符串替换掉，而是会产生一个新的字符串
# new_poetry = poetry.replace('说','乐')
# print(poetry)
# print(new_poetry)
# new_poetry = poetry.replace('说','乐',1)
# print(new_poetry)

# 容器专属方法——函数
# 字符串通过点的方式调用函数。

# 1.字符串一旦定义不允许修改
# 2.字符串容器中的元素都是字符串类型的

# 找到字符串中 @ 的位置
# 获得字符串中的子串
# user_email = 'zhengzheng@qq.com'
# # 如果查找到，返回子串第一次出现的位置
# # 如果查找不到 @,返回-1
# position = user_email.find('@')
# if position == -1:
#     print('@不存在，邮箱不合法')
# else:
#     print(position)


# # 字符串提供了一种语法，用来获取字符串中的一个子串
#
# user_email = 'zhengzheng@qq.com'
#
# print(user_email[0])
# # 切片语法，左闭右开
# print(user_email[0:3])
# print(user_email[0:10])
# # 获得容器元素个数
# string_lengh = len(user_email)
# print(user_email[4:string_lengh])
#
# # 起始值不写表示从0开始，结束值不写表示到最后
# print(user_email[:10])
# print(user_email[0:])
# print(user_email[:])
# # 步长
# print('*' * 30)
# print(user_email[0:10:2])
#
# # 起始 结束 步长都可以为负数
# print(user_email[-5:-1])
# print(user_email[6:1:-1])
# # 字符串逆序
# print(user_email[::-1])


# # 默认参数
# def my_function(num):
#     print('num',num)
#
# my_function(18)
# # 函数需要一个参数，调用的使用必须要传递一个参数

# 我们在给函数形参设置默认参数时，并不是会给所有的参数都设置默认参数
# 注意点：如果某一个位置形参设置了默认参数，那么该位置后面的所有参数都必须设置默认参数

# def my_num(a,b=20,c=30):
#     return a+b+c
#
# ret = my_num(10)
# ret = my_num(10,100)
# ret = my_num(10,100,1000)
# print(ret)


# user_email = 'zhengzheng@qq.com'
# # 如果查找到，返回子串第一次出现的位置
# # 如果查找不到 @,返回-1
# position = user_email.find('@')
# if position == -1:
#     print('@不存在，邮箱不合法')
# else:
#     username = user_email[:position]
#     houzhui = user_email[position+1:]
#     print('用户名是：',username)
#     print('邮箱后缀是：',houzhui)

# # split 拆分
# my_str = 'aa#b123#cc#dd'
# ret = my_str.split('#')
# print(ret)
# print(ret[0])
# print(ret[3])
#
# user_email = 'zhengzheng@qq.com'
# # 获取 @ 在字符串user_email中出现的次数
# char_count = user_email.count('@')
# if char_count > 1:
#     print('你的邮箱不合法！')
# else:
#     result = user_email.split('@')
#     print('用户名：',result[0])
#     print('邮箱后最：',result[1])

# # 获得用户的注册名
# register_name = input('请输入你的用户名：')
# # 去掉用户两边的空格
# register_name = register_name.strip()
# # 判断字符串是否全部为字母
# if register_name.isalpha():
#     print('恭喜你',register_name,'注册成功！')
# else:
#     print('注册失败！')


# 列表
# 字符串中的元素不能够修改，而且元素类型单一
# 列表中的元素可以修改，并且可以存放多种类型的元素

# my_list = []

# 创建一个带有数字类型元素的列表
# my_list = [10,20,30]

# 创建一个带有字符串类型元素的列表
# my_list = ['aa','bb','cc']

# 列表中可以再放另一个列表
# my_list = [[1,2,3],[4,5,6],[7,8,9]]

# 列表中可以放不同类型的元素
# my_list = ['hello',100,200,[5,6,5,6]]

# #  列表的而遍历操作
# my_list = [0,1,2,3,4,5,6,7,8,9]
# index = 0
# while index < 6:
#     print(my_list[index])
#     index += 1

# for循环一般用于容器中遍历
# for val in my_list:
#     print(val)

# # break continue 可以用在循环中
# my_list = [[1,2,3],[4,5,6],[7,8,9]]
# i = 0
# while i < len(my_list):
#      j = 0
#      while j < len(my_list[i]):
#          print(my_list[i][j])
#          j += 1
#      i += 1
#
# print('*'*30)
#
# for o in my_list:
#     for v in o:
#         print(v)

# # 创建一个包含10个随机数的列表
# import random
# my_list = []
#
# i = 0
# while i < 10:
#     # 产生随机数
#     random_number = random.randint(1,100)
#     # 将随机数插入到列表中
#     my_list.append(random_number)
#     i += 1
#
# print(my_list)
# # 对列表中的元素进行排序，sort 排序的意思
# # 默认排序是从小到大，升序排序
# my_list.sort()
# print(my_list)
# #将sort 函数的 reverse 默认值改为True，即可实现从大到小的排序
# my_list.sort(reverse=True)
# print(my_list)

# my_list = [1,2,3,4,5,676,7,8,9]
#
# old_value = 4
# new_value = 21
#
# # index 用于根据数据值进行查找，如果查询结果失败，则会报错
# if old_value in my_list:
#     # 查找到old_value 的位置
#     pos = my_list.index(old_value)
#     # 根据位置修改参数
#     my_list[pos] = new_value
#
# print(my_list)

# 练习:一个学校，三个办公室，八位老师随机分配工位

# # 定义学校和办公室
# import random
# school = [[],[],[]]
#
# def creat_teachers():
#     '''创建老师列表'''
#
#     # 定义列表保存老师
#     teacher_list = []
#
#     index = 1
#     while index <= 8:
#         # 创建老师的名字
#         teacher_name = '老师' + str(index)
#         # 把老师装进笼子里
#         teacher_list.append(teacher_name)
#         index += 1
#
#     return teacher_list
#
# techers_list = creat_teachers()
# # print(techers_list)
# # techers_list2 = creat_teachers()
# # print(techers_list2)
#
# # 分配老师
# for teacher in techers_list:
#     # 产生一个办公室编号的随机数
#     office_number = random.randint(0,2)
#     # 给老师随机分配办公室
#     school[office_number].append(teacher)
#
# # 查看各个办公室的老师
# for office in school:
#     for person in office:
#         print(person,end='  ')
#     print()


# # 元组可以从美国语法层面来限制数据的意外修改
# # 元组使用小括号来定义
# my_tuple = (10,20,30,40,50)
# print(my_tuple[0])
# # 注意：元组中只有一个元素的话，需要在元素后面添加括号
# my_tuple = (10,)
# # 元组可以嵌套元组
# my_tuple = ((3,4,5),(6,7,8))
# print(my_tuple)
# # 元组中的元素不能被修改
# my_tuple = (1,2,3)
# # my_tuple[0] = 100
#
# for v in my_tuple:
#     print(v)
#
# # 查询
# pos = my_tuple.index(3)
# print(pos)
#
# my_tuple = ((10,),)
# # 元组支持切片操作
# my_tuple = (1,4,3,5,2)
# print(my_tuple[1:])


# 字典
# 字典的查找效率很高，但是比较占内存，字典就是以空间换时间
# 字典的定义
def test01():
    my_dict = {'name':'Obama','age':18,'gender':'男',101:100}
    print(my_dict['name'])
    print(my_dict[101])  # key关键字   value值
    my_dict['gender'] = '女'
    print(my_dict)

# test01()

# 字典的键不能重复，值是可以重复的
# 字典是非序列式排序，不支持索引也不支持切片

def test02():
    """"不支持索引和切片"""

    my_dict = {'name': 'Obama', 'age': 18, 'gender': '男', 101: 100}
    print(my_dict[2])
    print(my_dict[1:])

# test02()

def test03():
    """获得字典的值"""

    my_dict = {'name': 'Obama', 'age': 18, 'gender': '男', 101: 100}
    # 使用括号这种访问字典元素的方式，如果键不存在会报错，程序终止
    # print(my_dict['age1'])
    # 使用 get 方法，如果 key 不存在默认返回 None ，  也可以返回指定默认值
    print(my_dict.get('age','返回值'))
    print(my_dict.get('name1'))

# test03()

def test04():
    """修改和添加元素"""

    my_dict = {'name': 'Obama', 'age': 18, 'gender': '男', 101: 100}
    # 如果 key 不存在是新增元素
    my_dict['score'] = 100  # 添加新元素
    print(my_dict)
    # 如果 key 存在就是修改元素
    my_dict['name'] = 'xiaoming'
    print(my_dict)

# test04()

# my_dict = {'name': 'Obama', 'age': 18, 'gender': '男', 101: 100}
#
# # del delete
# del my_dict['age']
# print(my_dict)
# my_dict.clear()
# print(my_dict)
#
# my_list = [1,2,34,4,5,6,7]
# del my_list[0]
# print(my_list)

my_dict = {'name': 'Obama', 'age': 18, 'gender': '男', 101: 100}

# 默认只能遍历出来键
# for v in my_dict:
#     print(v)

# # keys 放法获得所有的值列表
# key_list = my_dict.keys()
# print(key_list)
#
# value_list = my_dict.values()
# print(value_list)
#
# # keys 放法获得所有的值列表，每一个键值对都是一个列表
# key_value_list = my_dict.items()
# print(key_value_list)
#
# for key_value in key_value_list:
#     print('key:',key_value[0],'value:',key_value[1])