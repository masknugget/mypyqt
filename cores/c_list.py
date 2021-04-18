

class Clist(list):
    '''
        list是通过cython对象产生的，所以简单的重写方式是__dict__ 或者slots，
        普通的类，可以为类实例赋值任何属性，这些属性会存储在__dict__中，但数据通过字典(Hash)存储所占用的空间较大，效率较低，__slots__属性的出现就是为了解决上述问题
    '''
    __dict__ = []
    def __init__(self, *args, **kwargs):
        print(args)
        print(kwargs)


    def append(self, object) -> None:
        self.__dict__.append(object)


    def remove(self, object) -> None:
        ...

    def insert(self, index: int, object) -> None:
        ...



class Clist(list):
    '''
        list是通过cython对象产生的，所以简单的重写方式是__dict__ 或者slots，
        普通的类，可以为类实例赋值任何属性，这些属性会存储在__dict__中，但数据通过字典(Hash)存储所占用的空间较大，效率较低，__slots__属性的出现就是为了解决上述问题
    '''
    __dict__ = []
    def __init__(self, *args, **kwargs):
        print(args)
        print(kwargs)


    def append_1(self, object) -> None:
        self.append(object)


    def remove(self, object) -> None:
        ...

    def insert(self, index: int, object) -> None:
        ...


# 正确的方法

# Creating a List where
# deletion is not allowed
class MyList(UserList):

    # Function to stop deleltion
    # from List
    def remove(self, s=None):
        raise RuntimeError("Deletion not allowed")

        # Function to stop pop from

    # List
    def pop(self, s=None):
        raise RuntimeError("Deletion not allowed")

    # Driver's code


L = MyList([1, 2, 3, 4])

print("Original List")

# Inserting to List"
L.append(5)
print("After Insertion")
print(L)

# Deliting From List
L.remove()

