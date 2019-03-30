## 使用__slots__
class Student(object):
	pass

# 动态绑定属性
s = Student()
s.name = 'csp'
print(s.name)

# 给实例绑定一个方法
def set_age(self, age):
	self.age = age

from types import MethodType
s.set_age = MethodType(set_age, s) # 给实例绑定一个方法

s.set_age(25)
print(s.age)

# 给一个实例绑定的方法，对另一个实例是不起作用的
s2 = Student()
#s2.set_age(22)

# 给 class 绑定方法  所有实例都可调用
def set_score(self, score):
	self.score = score

Student.set_score = set_score

s.set_score(100)
print(s.score)

s2.set_score(99)
print(s2.score)



## __slots__
# 只允许对Student实例添加name和age属性
class Teacher(object):
	__slots__ = ('name', 'age')

t = Teacher()
# t.score = 99
# 使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的

## 使用@property
class Classmates(object):
	@property
	def score(self):
		return self._score

	@score.setter
	def score(self, value):
		if not isinstance(value, int):
			raise ValueError('score must be an integer!')
		if value < 0 or value > 100:
			raise ValueError('score must between 0 ~ 100!')
		self._score = value

c = Classmates()
c.score = 80
print(c.score)