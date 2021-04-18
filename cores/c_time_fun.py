import time


def func():
    print('func start')
    time.sleep(1)
    print('func end')


t = time.time()
func()
print(f'coast:{time.time() - t:.4f}s')




################
import time


def func():
    print('func start')
    # time.sleep(1)
    print('func end')


t = time.time()
func()
print(f'coast:{time.time() - t:.8f}s')



###########
import time


def func():
    print('func start')
    # time.sleep(1)
    print('func end')


t = time.perf_counter()
func()
print(f'coast:{time.perf_counter() - t:.8f}s')


##  timeit.timeit ()
import time
import timeit


def func():
    print('func start')
    time.sleep(1)
    print('func end')


print(timeit.timeit(stmt=func, number=1))


########## 装饰器统计运行耗时
import time


def coast_time(func):
    def fun(*args, **kwargs):
        t = time.perf_counter()
        result = func(*args, **kwargs)
        print(f'func {func.__name__} coast time:{time.perf_counter() - t:.8f} s')
        return result

    return fun


@coast_time
def test():
    print('func start')
    time.sleep(2)
    print('func end')


if __name__ == '__main__':
    test()



### 如果有使用异步函数的需求也可以加上

import asyncio
import time
from asyncio.coroutines import iscoroutinefunction


def coast_time(func):
    def fun(*args, **kwargs):
        t = time.perf_counter()
        result = func(*args, **kwargs)
        print(f'func {func.__name__} coast time:{time.perf_counter() - t:.8f} s')
        return result

    async def func_async(*args, **kwargs):
        t = time.perf_counter()
        result = await func(*args, **kwargs)
        print(f'func {func.__name__} coast time:{time.perf_counter() - t:.8f} s')
        return result

    if iscoroutinefunction(func):
        return func_async
    else:
        return fun


@coast_time
def test():
    print('func start')
    time.sleep(2)
    print('func end')


@coast_time
async def test_async():
    print('async func start')
    await asyncio.sleep(2)
    print('async func end')


if __name__ == '__main__':
    test()
    asyncio.get_event_loop().run_until_complete(test_async())



key_value ={'a': 1, 'a': 2, 'b':2}
sorted(key_value.items(), key = lambda kv:(kv[1], kv[0]))
## with 语句统计运行耗时
import asyncio
import time


class CoastTime(object):
    def __init__(self):
        self.t = 0

    def __enter__(self):
        self.t = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f'coast time:{time.perf_counter() - self.t:.8f} s')


def test():
    print('func start')
    with CoastTime():
        time.sleep(2)
        print('func end')


async def test_async():
    print('async func start')
    with CoastTime():
        await asyncio.sleep(2)
        print('async func end')


if __name__ == '__main__':
    test()
    asyncio.get_event_loop().run_until_complete(test_async())
