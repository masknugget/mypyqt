class Singleton(object):
    def __new__(cls,*args, **kwargs):
        if not hasattr(cls,'_inst'):
            print(cls)
            cls._inst = super(Singleton, cls).__new__(cls)
        return cls._inst


