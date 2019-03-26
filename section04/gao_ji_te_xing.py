## 切片
# L[0:3]表示，从索引0开始取，直到索引3为止，但不包括索引3
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
print(L[0:3])

L = list(range(100))
# print(L)
# 可以通过切片轻松取出某一段数列。比如前10个数：
print(L[:10])
# 后10个数：
print(L[-10:])
# 前11-20个数：
print(L[10:20])
# 前10个数，每两个取一个：
print(L[:10:2])
# 所有数，每5个取一个：
print(L[::5])
# tuple也是一种list，唯一区别是tuple不可变。因此tuple也可以用切片操作，只是操作的结果仍是tuple：
# 


## 迭代
from collections.abc import Iterable
print(isinstance('abc', Iterable))
print(isinstance([1, 2, 3], Iterable))
print(isinstance(123, Iterable))

for ch in 'ABC':
	print(ch)


for x, y in [(1,1), (2,4),(3,9)]:
	print(x, y)


## 列表生成器
# 列表生成式即List Comprehensions，是Python内置的非常简单却强大的可以用来创建list的生成式。
print([x * x for x in range(1,11) if x % 2 == 0])
print([m + n for m in 'ABC' for n in 'XYZ'])

## 生成器
# 在Python中，这种一边循环一边计算的机制，称为生成器：generator。
# 要创建一个generator，有很多种方法。
# 第一种方法很简单，只要把一个列表生成式的[]改成()，就创建了一个generator：
g = (x * x for x in range(10))
for n in g:
	print(n)

# 这就是定义generator的另一种方法。
# 如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator：
def fib(max):
	n, a, b = 0, 0, 1
	while n < max:
		yield b
		a, b = b, a + b
		n = n + 1
	return 'done'
# 这里，最难理解的就是generator和函数的执行流程不一样。
# 函数是顺序执行，遇到return语句或者最后一行函数语句就返回。
# 而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，
# 再次执行时从上次返回的yield语句处继续执行。

def triangles():
	L = [1]
	yield L
	while True:
		n = 0
		T = []
		while True:
			if n == 0:
				T.append(1)
			if n == len(L) - 1:
				T.append(1)
				break
			T.append(L[n] + L[n + 1])
			n = n + 1
		L = T
		yield L

s = 0
for t in triangles():
    print(t)
    s = s + 1
    if s == 10:
        break
print()

## 迭代器
# 凡是可作用于for循环的对象都是Iterable类型；
# 凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；
# 集合数据类型如list、dict、str等是Iterable但不是Iterator，
# 不过可以通过iter()函数获得一个Iterator对象。