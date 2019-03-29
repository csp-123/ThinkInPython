## 类和实例
class Student(object):
	
	def __init__(self, name, score):
		self.__name = name
		self.__score = score

	def get_name(self):
		return self.__name

	def get_score(self):
		return self.__score

	def set_name(self, name):
		self.__name = name

	def set_score(self, score):
		self.__score = score

	def print_score(self):
		print('%s:%s' %(self.__name, self.__score))
bart = Student('csp', 50)
bart.print_score()

## 访问限制
# 如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__，
# 在Python中，实例的变量名如果以__开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问
# 不能直接访问__name是因为Python解释器对外把__name变量改成了_Student__name
# 但是强烈建议你不要这么干，因为不同版本的Python解释器可能会把__name改成不同的变量名。


## 继承和多态
class Animal(object):
	def run(self):
		print('animal is running...')

class Dog(Animal):
	def run(self):
		print('dog is running...')
		
class Cat(Animal):
	def run(self):
		print('cat is running...')
Dog().run()
Cat().run()

# 继承可以把父类的所有功能都直接拿过来，这样就不必重零做起，
# 子类只需要新增自己特有的方法，也可以把父类不适合的方法覆盖重写。
# 动态语言的鸭子类型特点决定了继承不像静态语言那样是必须的

## 获取对象信息
# 使用type()
print(type(123))
print(type(abs))
print(type('str'))

import types
def fn():
	pass

print(type(fn) == types.FunctionType)
print(type(abs)==types.BuiltinFunctionType)
print(type(lambda x: x)==types.LambdaType)
print(type((x for x in range(10)))==types.GeneratorType)

## 使用isinstance()
print('----isinstance----')
print(isinstance(Dog(), Dog))
print(isinstance(Dog(), Animal))
print(isinstance([1, 2, 3], (list, tuple)))

## 使用dir()
# 如果要获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list
print('----dir()----')
print(dir('ABC'))

class MyDog(object):
	def __len__(self):
		return 100
dog = MyDog()
print(len(dog))

## 类属性和实例属性
# 在编写程序的时候，千万不要对实例属性和类属性使用相同的名字，
# 因为相同名称的实例属性将屏蔽掉类属性，但是当你删除实例属性后，
# 再使用相同的名称，访问到的将是类属性