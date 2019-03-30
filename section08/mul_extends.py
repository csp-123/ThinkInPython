## MixIn
class Aminal(object):
	def run(self):
		print('animal run')

class DogMixIn(object):
	def eat(self):
		print('dog eat meat')

class CatMixIn(object):
	def eat(self):
		print('cat eat meat')
		
class Test(Aminal, CatMixIn, DogMixIn):
	pass

t = Test()
t.run()
t.eat() # 重名方法按照继承先后调用

## __str__ 类似toString
class Student(object):
	"""docstring for Student"""
	def __init__(self, name):
		self.name = name

	def __str__(self):
		return 'Student object (name: %s)' %self.name
	__repr__ = __str__

	def __getattr__(self, attr):
		if attr == 'score':
			return 99

	def __call__(self):
		print('My name is %s.' % self.name)
print(Student('csp'))
s = Student('ccp')
print('score: ', s.score)
s()

## __iter__
# 如果一个类想被用于for ... in循环，类似list或tuple那样，就必须实现一个__iter__()方法，
# 该方法返回一个迭代对象，然后，Python的for循环就会不断调用该迭代对象的__next__()方法拿到循环的下一个值，
# 直到遇到StopIteration错误时退出循环。	
class Fib(object):
	"""docstring for Fib"""
	def __init__(self):
		self.a, self.b = 0, 1

	def __iter__(self):
		return self

	def __next__(self):
		self.a, self.b = self.b, self.a + self.b
		if self.a > 1000:
			raise StopIteration
		return self.a
	def __getitem__(self, n):
		a, b = 1, 1
		for x in range(n):
			a, b = b, a + b
		return a

for x in Fib():
	print(x)
		
## __getitem__
print('__getitem__: %d' %Fib()[10])

## __getattr__
## __call__