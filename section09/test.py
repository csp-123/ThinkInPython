## 错误处理
try:
	print('try...')
	r = 10 / 0
	print('result: ', r)
except ZeroDivisionError as e:
	print('except: ', e)
finally:
	print('finally...')

print('END')


try:
	print('try...')
	r = 10 / int('2')
	print('result:', r)
except ValueError as e:
	print('ValueError:', e)
except ZeroDivisionError as e:
	print('ZeroDivisionError:', e)
else:
	print('no error!')
finally:
	print('finally...')
print('END')

# Python所有的错误都是从BaseException类派生的

## 调用栈
import logging
def foo(s):
	return 10 / int(s)

def bar(s):
	return foo(s) * 2

def main():
	try:
		bar('0')
	except Exception as e:
		logging.exception(e)

main()

## 记录错误 logging

## 抛出错误 raise


## 断言
def foo(s):
	n = int(s)
	assert n != 0, 'n is zero!'
	return 10 / n

def main():
	foo('0')
main()
# assert的意思是，表达式n != 0应该是True，否则，根据程序运行的逻辑，后面的代码肯定会出错
# 程序中如果到处充斥着assert，和print()相比也好不到哪去。不过，启动Python解释器时可以用-O参数来关闭assert
# 