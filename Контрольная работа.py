import functools
import random
from itertools import islice

def count_calls(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.c += 1
        return func(*args, **kwargs)

    wrapper.c = 0
    return wrapper

@count_calls
def f(x):
    return(x+1)


@count_calls
def g(x, y):
    return x + y

def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

def quicksort(res):
    if len(res) <= 1:
        return res
    ser = res[len(res) // 2]
    l = [x for x in res if x < ser]
    m = [x for x in res if x == ser]
    r = [x for x in res if x > ser]
    return quicksort(l) + m + quicksort(r)


#Задание 1
f(3)
f(4)
g(6, 7)
print("f вызвали:", f.c)
print("g вызвали:", g.c)

# Задание 2
print("Фибоначчи:", list(islice(fib(), 15)))

# Задание 3
data = [random.randint(0, 1000) for i in range(0, 1000)]
print("Cортировка:", quicksort(data))
