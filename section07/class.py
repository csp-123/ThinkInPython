## 类和实例
class Student(object):
	
	def __init__(self, name, score):
		self.name = name
		self.score = score

	def print_score(self):
		print('%s:%s' %(self.name, self.score))
bart = Student('csp', 50)
print(bart)
bart.print_score()

