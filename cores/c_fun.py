import inspect

def fun_add(x, y) -> int:
    '''
        这是什么
    :param x:
    :param y:
    :return:
    '''
    return x + y


name = fun_add.__name__
doc = fun_add.__doc__
fun_add.__qualname__
fun_add.__dict__
fun_add.__code__
fun_add.__kwdefaults__
fun_add.__annotations__     # 注解返回


# 获得函数的参数
inspect.signature(fun_add).parameters