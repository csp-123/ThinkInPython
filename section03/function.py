import math
# 内置函数 http://docs.python.org/3/library/functions.html#abs 官方文档

## 定义函数
# 在Python中，定义一个函数要使用def语句，依次写出函数名、括号、括号中的参数和冒号:，
# 然后，在缩进块中编写函数体，函数的返回值用return语句返回。
def my_abs(x):
	if not isinstance(x, (int, float)):
		raise TypeError('bad operand type')
	if x >= 0:
		return x
	else:
		return -x

print(my_abs(-10))
#print(my_abs('asd'))

## 返回多个值

def move(x, y, step, angle = 0):
	nx = x + step * math.cos(angle)
	ny = y - step * math.sin(angle)
	return nx, ny

x, y = move(100, 100, 60, math.pi/6)
print(x, y)

## 函数的参数
## 默认参数
# 默认参数降低了函数调用的难度，而一旦需要更复杂的调用时，
# 又可以传递更多的参数来实现。无论是简单调用还是复杂调用，函数只需要定义一个。
#  定义默认参数要牢记一点：默认参数必须指向不变对象！
def power(x, n = 2):
	s = 1
	while n > 0:
		n = n - 1
		s = s * x
	return s

print(power(5, 3))

## 可变参数
def calc(*numbers):
	sum = 0;
	for n in numbers:
		sum += n * n
	return sum

print(calc(1, 2))
print(calc())
# *nums表示把nums这个list的所有元素作为可变参数传进去。这种写法相当有用，而且很常见
nums = [1, 2, 3]
print(calc(*nums))

## 关键字参数
# 可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。
# 而关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict
def person(name, age, **kw):
	print('name:', name, 'age:', age, 'other:', kw)

person('csp', 26)
person('ccp', 36, city = 'BeiJing')
person('ssp', 16, gender = 'M', job = 'Engineer')
# 简化写法
extra = {'city': 'Beijing', 'job': 'Engineer'}
person('ppp', 24, **extra)



## 命名关键字参数
# 如果要限制关键字参数的名字，就可以用命名关键字参数，
# 例如，只接收city和job作为关键字参数。这种方式定义的函数如下：
# 和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数
def person(name, age, *, city, job):
	print(name, age, city, job)

person('Jack', 24, city='BeiJing', job='Engineer')

# 如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了：
# 命名关键字参数必须传入参数名，这和位置参数不同。
# 使用命名关键字参数时，要特别注意，如果没有可变参数，就必须加一个*作为特殊分隔符。
# 如果缺少*，Python解释器将无法识别位置参数和命名关键字参数：

## 参数组合
# 在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，
# 这5种参数都可以组合使用。但是请注意，
# 参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
