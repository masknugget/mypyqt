class A:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


    def __get__(self, instance, owner):
        print(instance, owner)
        return 1

    def __getattr__(self, item):
        '''
        a.v的值为2
        :param item:
        :return:
        '''
        print('getattr', item)
        return 2

    def __setattr__(self, key, value):
        '''
        a.v = val 这个可以
        :param key:
        :param value:
        :return:
        '''
        print('set attr')
        self.__dict__[key] = value


    # def __getattribute__(self, item):
    #     '''
    #     a.x 的值为3
    #     :param item:
    #     :return:
    #     '''
    #     print('getattribute ', item)
    #     return 3
    #



a = A(1, 2, 3)

a.x
a.v