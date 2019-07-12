# test5 2019/7/8  容器

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


poetry = '有朋自远方来，不亦说乎.说'

# replace并不会把原来的字符串替换掉，而是会产生一个新的字符串
new_poetry = poetry.replace('说','乐')
print(poetry)
print(new_poetry)
new_poetry = poetry.replace('说','乐',1)
print(new_poetry)

# 容器专属方法——函数
# 字符串通过点的方式条用函数。

# 1.字符串一旦定义不允许修改
# 2.字符串容器中的元素都是字符串类型的