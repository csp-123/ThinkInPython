## Thread
import time, threading

# 新线程执行的代码
def loop():
	print('thread %s is running...' % threading.current_thread().name)
	n = 0
	while n < 5:
		n = n + 1
		print('thread %s >>> %s' % (threading.current_thread().name, n))
		time.sleep(0.5)
	print('thread %s ended.' % threading.current_thread().name)

print('thread %s is running...' % threading.current_thread().name)

t = threading.Thread(target=loop, name='LoopThread')
t.start()
t.join()
print('thread %s ended.' % threading.current_thread().name)


## Lock
print()
print('-----Lock----')
balance = 0
lock = threading.Lock()
def change_it(n):
	global balance
	balance = balance + n
	balance = balance - n

def run_thread(n):
	for x in range(100000):
		lock.acquire()
		try:
			change_it(n)
		finally:
			lock.release()
t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(7,))
t3 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t3.start()
# t1.join()
# t2.join()
# t3.join()
time.sleep(5)
print(balance)

# Python解释器由于设计时有GIL全局锁，导致了多线程无法利用多核。
# 多线程的并发在Python中就是一个美丽的梦。

# ThreadLocal
# 创建全局ThreadLocal对象:
local_school = threading.local()

def process_student():
	# 获取当前线程关联的student:
	std = local_school.student
	print('Hello, %s (in %s)' % (std, threading.current_thread().name))

def process_thread(name):
	# 绑定ThreadLocal的student:
	local_school.student = name
	process_student()

t1 = threading.Thread(target= process_thread, args=('Alice',), name='Thread-A')
t2 = threading.Thread(target= process_thread, args=('Bob',), name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()