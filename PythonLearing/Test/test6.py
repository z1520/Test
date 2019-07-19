# test6 2019/7/14
"""
学习内容：
类和对象 - 什么是类 / 什么是对象 / 面向对象其他相关概念
定义类 - 基本结构 / 属性和方法 / 构造器 / 析构器 / __str__方法
使用对象 - 创建对象 / 给对象发消息
面向对象的四大支柱 - 抽象 / 封装 / 继承 / 多态
属性 - 类属性 / 实例属性 / 属性访问器 / 属性修改器 / 属性删除器 / 使用__slots__
类中的方法 - 实例方法 / 类方法 / 静态方法
继承和多态 - 什么是继承 / 继承的语法 / 调用父类方法 / 方法重写 / 类型判定 / 多重继承 /

"""
# 1.对象：对象 = 属性（静态） + 方法（动态）
#   属性一般是一个个变量，方法是一个个函数
#   类的属性 就是 类变量
#   实例变量：定义在方法中的变量，只作用于当前实例的变量

# python中的类名约定以大写字母开头
class Turtle:
    # 关于类的简单例子
    # 属性 == 类变量
    color = "green"
    weight = "10kg"
    legs = 4
    shell = True
    mouth = 'big'
    # 方法
    def climb(self):
        self.name = 'test'  # 实例变量，定义在方法中的变量，只作用于当前实例的类
        print('我在很努力的爬！')

    def run(self):
        print('我在很努力的跑！')

    def bite(self):
        print('我要')

    def sleep(self):
        print('我要睡觉了！')

# # 创建一个实例对象，也就是类的实例化
# tt = Turtle()  #类的实例化，也就是创建一个对象，类名约定大写字母开头
# # 创建好类后就能调用类里面的方法了
# tt.bite()
# tt.sleep()

# 面向对象的特征
# 1.封装（信息隐蔽技术）
# python的列表list其实就是一个对象，它提供了很多方法：sort（）  append（）
# 封装后就可以直接调用里面的方法了
# 2.继承
# 子类自动共享父类之间数据和方法的机制

# 创建一个类继承list的所有的方法和属性
class Mylist(list):
    pass
# 类的实例化
list1 = Mylist()
# 继承后调用list的方法append（）
list1.append(1)

# 3.多态
# 不同对象对同一方法响应不同行动。就是名字一样方法不一样：
class A:
    def fun(self):
        print('aaa')
class B:
    def fun(self):
        print('bbb')

a = A()
b = B()
# a.fun()
# b.fun()

# 面向对象的特征
# oo = Object Oriented  # 面向对象


# self是什么？
#当对象方法被调用时，对象会将自己作为第一个参数传给self，python就是根据self知道哪一个对象在调用方法
class Ball():
    def setname(self,name):
        self.name = name
    def kick (self):
        print('我叫%r，谁踢我。'%self.name)

a = Ball()  # 实例化生成 a 对象
a.setname('a')  # 调用方法设名为 a
b = Ball()
b.setname('b')
c = Ball()
c.setname('c')
# 通过self知道是哪个对象调用kick的方法
# a.kick()
# b.kick()


# python 的魔法方法：
# __init__(self) 这是个构造方法。
# 实例化一个对象时，这个方法就会在对象创建时（实例化类就是创建对象）自动调用。实例化时就会调用__init__(self)这个方法
# 实例化对象时可以传入参数的，这些参数被传入init方法中，可通过重写方法来自定义对象初始化操作。

class Ball():
    def __init__(self,name):
        self.name = name
    def kick (self):
        print('我叫%r，谁踢我。'%self.name)

b = Ball('b') #创建对象，这时__init__(self)：就被调用了，可以传入 b
# b.kick()

# 公有私有
# 公有：python中对象的属性和方法都是公开的，都是公有的，通过.操作符来访问
# 私有：python中定义私有变量只需要在变量名或函数名前增加两个下划线‘__’ ，那么这个函数，变量变成私有的了

class A():
    __name = 'z1520'  # 私有变量，外部不能通过.操作符直接访问

# 继承
# class A（B）：
#   ......
# B我们叫父类，基类或者超类
# A我们叫子类，子类继承父类的属性和方法

class Parent():
    def hello(self):
        print('helloworld')

class Child(Parent):
    pass

p = Parent()
# p.hello()
c = Child()
# c.hello()
# 注意：如果子类中定义与父类同名的方法或者属性，则会自动覆盖父类对应的方法或属性

class Parent():
    def hello(self):
        print('helloworld')

class Child(Parent):
    def hello(self):
        print('hahaha')

p = Parent()
# p.hello()
c = Child()
# c.hello()  # 子类和父类方法相同，（子类重写父类方法）会覆盖父类方法，但是父类自己的方法不变

# super()函数：解决了子类就算重写父类方法或属性仍然可以继续使用父类的方法和属性

import random as r
# 利用继承演示鱼游动的方向
class Fish():  # 父类
    def __init__(self):
        self.x = r.randint(0,10)
        self.y = r.randint(0,10)

    def move(self):
        self.x -= 1  # 一直向西移动
        print('我的位置：',self.x,self.y)

class Goldfish(Fish):  # 子类
    pass

class Carp(Fish):
    pass

class Salmon(Fish):
    pass

class Shark(Fish):
    def __init__(self):  # 这里重写了一个__init__方法，就会覆盖掉父类的方法，用到super函数后就可以继续使用父类的方法
    # super函数不用给定任何基类的名字(如下)，它会一层层找出代码所有父类里面对应的方法，要求改变该类的继承关系时只需要修改这个类的父类就行（就是括号里面的Fish）
        super().__init__()  # super（）.重写的属性或者方法
        self.hungry = True

    def eat(self):
        if self.hungry:
            print('我要开始吃了哦！')
            self.hungry = False
        else:
            print('饱了，吃不下了！')

# f = Fish()
# f.move()
# g = Goldfish()
# g.move()
# s = Salmon()
# s.move()
# s = Shark()
# s.move()
# s.eat()
# s.eat()
# s.move()  # 这就是子类就可以使用父类的move（）方法

# 组合：一般把几个没有什么关系的类放在一起使用时通过组合类的方法
# 要求定义一个类，叫水池，水池里面有乌龟和鱼
class Turtle():  # 定义乌龟类
    def __init__(self,x):
        self.mun = x

class Fish():  # 定义鱼类
    def __init__(self,y):
        self.num = y

class Poor():  # 定义水
    def __init__(self,x,y):

        # 直接把需要的类在这里实例化，实现组合
        self.turtle = Turtle(x)
        self.fish = Fish(y)

    def print_num(self):
        print('水池里面总共有乌龟%d只，小鱼%r条！'%(self.turtle.mun,self.fish.num))

p = Poor(3,10)
# p.print_num()

# 组合就是把类的实例化放到一个新类里，他就把旧类组合进去了


# 类，类对象，实例对象
class C():  # 类，当类写完后就变成了对象
    def x(self):
        print('xaaa')

# c = C()  # c是实例对象，C()是类对象
# c.x()
#
# c.x = 1  # 实例对象初始化一个变量
# c.x
# c.x()  # 就不能继续调用原来的方法了，同名讳覆盖掉类的方法

# 所以：不要试图在一个类里面定义所有的属性和方法，应该利用继承和组合机制
# 用不同的词性命名，如属性用名词，方法用动词


# 什么是绑定？
# python严格要求方法需要有实例才能被调用，这种限制其实就是绑定

class CC():  # 类
    def setxy(self,x,y):
        self.x = x
        self.y = y
    def printxy(self):
        print(self.x,self.y)

dd = CC()  # 实例对象，类对象
# dd.__dict__  # 查看实例对象所拥有的属性
# CC.__dict__  # 查看类对象所拥有的属性

dd.setxy(4,5)  #实例对象中传入参数x，y
# dd.__dict__  # 实例对象就有属性了，这两个属性仅属于实例对象的，；类对象中是没有的
# CC.__dict__
# 类对象中是没有实例对象传入的，这归功于绑定功能

# 为什么实例对象调用方法后类对象中没有实例对象的属性？
# 实例对象调用方法时，dd.setxy(dd,4,5)实际上是这样的，也就是(self.x = x;self.y = y) dd.x = 4,dd.y = 5,那么4，5存放在实例对象的空间，所以这两个属性只属于实例对象的/
# 实例对象调用方法时，先把自己传给self，self.x也就是dd.x


# 类对象和实例对象的差别：
# 把类对象CC删除后，del CC，再实例化就会报错，但是已经实例化对象dd仍然可以调用类对象中的方法：
del CC
dd.setxy(3,4)
# dd.__dict__

# # dd = CC()
# dd.printxy()

# 为什么已经实例化对象dd仍然可以调用类对象的方法？
# 类中定义的属性是静态属性，方法也一样，就算类对象被删除了，属性和方法也一样存放在内存中，故实例对象仍然可以从内存中调用类的方法和属性，除非程序退出。
# 所以创建一个类后最好先实例化再使用类对象中的方法，不要直接利用类对象调用方法