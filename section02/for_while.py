names = ['csp', 'ccp', 'ssp']
for name in names :
	print(name)


sum = 0
for x in range(101):
	sum += x
print(sum)

sum = 0
n = 99
while n > 0:
	sum += n
	n = n - 2
print(sum)

# break语句可以在循环过程中直接退出循环，而continue语句可以提前结束本轮循环，
# 并直接开始下一轮循环。这两个语句通常都必须配合if语句使用。

# 要特别注意，不要滥用break和continue语句。break和continue会造成代码执行逻辑分叉过多，
# 容易出错。大多数循环并不需要用到break和continue语句，上面的两个例子，
# 都可以通过改写循环条件或者修改循环逻辑，去掉break和continue语句。