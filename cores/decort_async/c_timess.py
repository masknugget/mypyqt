# 任务超时退出

import functools
from concurrent import futures

executor = futures.ThreadPoolExecutor(1)

def timeout(seconds):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            future = executor.submit(func, *args, **kw)
            return future.result(timeout=seconds)
        return wrapper
    return decorator


import time

@timeout(1)
def task(a, b):
    time.sleep(1.2)
    return a+b

task(2, 3)

@timeout(1)
def task(a, b):
    time.sleep(0.9)
    return a+b

task(2, 3)



import functools
from concurrent import futures

class timeout:
    __executor = futures.ThreadPoolExecutor(1)

    def __init__(self, seconds):
        self.seconds = seconds

    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            future = timeout.__executor.submit(func, *args, **kw)
            return future.result(timeout=self.seconds)
        return wrapper



## 日志记录

import time
import functools


def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        res = func(*args, **kwargs)
        end = time.perf_counter()
        print(f'函数 {func.__name__} 耗时 {(end - start) * 1000} ms')
        return res

    return wrapper


@log
def now():
    print('2021-7-1')


now()



## 缓存
import math
import random
import time


def task(x):
    time.sleep(0.01)
    return round(math.log(x**3 / 15), 4)



from functools import lru_cache

@lru_cache()
def task(x):
    time.sleep(0.01)
    return round(math.log(x**3 / 15), 4)



## 约束某个函数的可执行次数

import functools


class allow_count:
    def __init__(self, count):
        self.count = count
        self.i = 0

    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            if self.i >= self.count:
                return
            self.i += 1
            return func(*args, **kw)
        return wrapper



@allow_count(3)
def job(x):
    x += 1
    return x


for i in range(5):
    print(job(i))

