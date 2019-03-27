# 高阶函数
# 变量可以指向函数
# 函数名也是变量
# 传入函数
# 既然变量可以指向函数，函数的参数能接收变量，
# 那么一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数。

## map/reduce
# Python内建了map()和reduce()函数。
# map()函数接收两个参数，一个是函数，一个是Iterable，
# map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回
def f(x):
	return x * x

r = map(f, range(1, 10))
print(list(r))

print(list(map(str, range(1, 10))))

# reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，
# 这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算
# reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
from functools import reduce
def g(x, y):
	return x + y
print(reduce(g, range(1,10)))

## filter
def is_odd(n):
	return n % 2 == 1
print(list(filter(is_odd, range(1, 15))))

# 用filter求素数
def _odd_iter():
	n = 1
	while True:
		n = n + 2
		yield n

def _not_divisible(n):
	return lambda x: x % n > 0

def primes():
	yield 2
	it = _odd_iter() # 初始化序列
	while True:
		n = next(it)
		yield n
		it = filter(_not_divisible(n), it) # 构造新序列

for n in primes():
	if n < 1000:
		print(n)
	else:
		break

## sorted
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower))
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True))