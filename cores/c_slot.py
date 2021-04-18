class Base(object):
    __slots__ = ()


class Child(Base):
    __slots__ = ('a',)


c = Child()
c.a = 'a'

c.b = 'b' # 出现错误



class SlottedWithDict(Child):
    __slots__ = ('__dict__', 'b')

swd = SlottedWithDict()
swd.a = 'a'
swd.b = 'b'
swd.c = 'c'


from abc import ABC

class AbstractA(ABC):
    __slots__ = ()

class BaseA(AbstractA):
    __slots__ = ('a',)

class AbstractB(ABC):
    __slots__ = ()

class BaseB(AbstractB):
    __slots__ = ('b',)

class Child(AbstractA, AbstractB):
    __slots__ = ('a', 'b')

c = Child() # no problem!




class Foo(object):
    __slots__ = 'bar', 'baz', '__dict__'


## Set to empty tuple when subclassing a namedtuple

from collections import namedtuple
class MyNT(namedtuple('MyNT', 'bar baz')):
    """MyNT is an immutable and lightweight object"""
    __slots__ = ()


nt = MyNT('bar', 'baz')
nt.bar
nt.baz

nt.quux = 'quux'  # 出现了属性错误



## __slot__作为基类

class AbstractBase:
    __slots__ = ()
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __repr__(self):
        return f'{type(self).__name__}({repr(self.a)}, {repr(self.b)})'



class Foo(AbstractBase):
    __slots__ = 'a', 'b'


class AbstractBaseC:
    __slots__ = ()
    @property
    def c(self):
        print('getting c!')
        return self._c
    @c.setter
    def c(self, arg):
        print('setting c!')
        self._c = arg


class Concretion(AbstractBase, AbstractBaseC):
    __slots__ = 'a b _c'.split()




class Student(object):
    ## 内存更加少
    __slots__ = ('name', 'gender', 'score')
    def __init__(self, name, gender, score):
        self.name = name
        self.gender = gender
        self.score = score