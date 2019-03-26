# 使用list 和 tuple
# Python内置的一种数据类型是列表：list。list是一种有序的集合，可以随时添加和删除其中的元素。
classmates = ['csp','ccp','ssp']
print(classmates)
print(classmates[1])
classmates.append('ppp')
print(classmates)

L = ['Apple', 123, True]
print(L)

# 多维list
s = ['python', 'java', ['asp', 'php'], 'scheme']
print(len(s))

# tuple
# 另一种有序列表叫元组：tuple。tuple和list非常类似，
# 但是tuple一旦初始化就不能修改，比如同样是列出同学的名字：
classmates = ('csp','ccp', 'ssp')
print(classmates)
# 定义的不是tuple，是1这个数！这是因为括号()既可以表示tuple，
# 又可以表示数学公式中的小括号，这就产生了歧义，因此，Python规定，
# 这种情况下，按小括号进行计算，计算结果自然是1
# 所以，只有1个元素的tuple定义时必须加一个逗号,，来消除歧义：
t=(1)
print(t)
t=(1,)
print(t)

# 表面上看，tuple的元素确实变了，但其实变的不是tuple的元素，而是list的元素
# tuple所谓的“不变”是说，tuple的每个元素，指向永远不变
t = ('a', 'b', ['A', 'B'])
t[2][0] = 'X'
t[2][1] = 'Y'
print(t)
