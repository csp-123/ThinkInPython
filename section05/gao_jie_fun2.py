## 返回函数
def calc_sum(*args):
	ax = 0
	for x in args:
		ax += x
	return ax

print(calc_sum(*range(1, 11)))

def lazy_sum(*args):
	def sum():
		ax = 0
		for x in args:
			ax += x
		return ax
	return sum
f = lazy_sum(*range(1, 11))
print(f())
# 在这个例子中，我们在函数lazy_sum中又定义了函数sum，并且，
# 内部函数sum可以引用外部函数lazy_sum的参数和局部变量，当lazy_sum返回函数sum时，
# 相关参数和变量都保存在返回的函数中，这种称为“闭包（Closure）”的程序结构拥有极大的威力。
# 当我们调用lazy_sum()时，每次调用都会返回一个新的函数

## 闭包
# 返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量。
def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs
f = count()
# 因为延迟执行  所以结果相同
print(f[0]())
print(f[1]())
print(f[2]())

# 解决此问题的办法是 
# 再创建一个函数，用该函数的参数绑定循环变量当前的值，无论该循环变量后续如何更改，已绑定到函数参数的值不变
def count():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
    return fs
f = count()
print(f[0]())
print(f[1]())
print(f[2]())




## 匿名函数
# 关键字lambda表示匿名函数，冒号前面的x表示函数参数。
# 匿名函数有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果。
# 用匿名函数有个好处，因为函数没有名字，不必担心函数名冲突。
print(list(map(lambda x: x * x, range(1, 11))))


## 装饰器
def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper
# 由于log()是一个decorator，返回一个函数，所以，原来的now()函数仍然存在，
# 只是现在同名的now变量指向了新的函数，于是调用now()将执行新函数，即在log()函数中返回的wrapper()函数。
@log
def now():
	print('2019-03-27')
f = now
f()
print(f.__name__)


## 偏函数
# functools.partial就是帮助我们创建一个偏函数的，不需要我们自己定义int2()，
# 可以直接使用下面的代码创建一个新的函数int2：
import functools
int2 = functools.partial(int, base=2)
print(int2('1000000'))

