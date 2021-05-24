class A:
    def __init__(self):
        self.v = 1


    def a(self):
        return 1


    def b(self):
        return 2



class B(A):
    def c(self):
        return 3


class B(A):
    def __init__(self):
        super(B, self).__init__()

    def c(self):
        return 3




d = A()
c = B()

d == c  # False


class Person(object):
    """
     定义一个人的类
    """
    country = 'China'
    def __init__(self,name):
        self.name = name

p = Person('liming')
p.age = 18


setattr(p,'age',18)
#三个参数分别为需要设置属性的对象，属性的名称（字符串）以及属性的值


if hasattr(p,'age'):
    #第一个参数为对象名，第二个参数为属性名（字符串）
    print("True")
else:
    print('False')
#True



import types
def run(self):
    print("%s在奔跑" % self.name)

p.run = types.MethodType(run,p)
#第一个参数是要添加的方法，第二个参数是对象
p.run()
#liming在奔跑




@classmethod
def greet(cls):
    print('I come from %s' % cls.country)
Person.greet = greet
Person.greet()
#I come from China



@staticmethod
def sleep():
    print('sleeping')
Person.sleep = sleep
Person.sleep()
#sleeping


del p.name
delattr(p,'run')


class student(object):
    __slots__ = ('name','run','age','country')
    #由于初始化函数中使用到了name，所以__slots__中必须添加name
    def __init__(self,name):
        self.name = name

s = student('xiaohong')
setattr(s,'age',18)
s.run = run
s.height = 170
#报错
