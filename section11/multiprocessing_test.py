## multiprocessing
import os

print('Process (%s) start...'% os.getpid())

from multiprocessing import Process

# 子进程要执行的代码
def run_proc(name):
	print('Run child process %s (%s)' % (name, os.getpid()))

if __name__ == '__main__':
	print('Parent process %s.' % os.getpid())
	p = Process(target=run_proc, args=('test',))
	print('child process will start.')
	p.start()
	p.join()
	print('Child process end.')

# 创建子进程时，只需要传入一个执行函数和函数的参数，
# 创建一个Process实例，用start()方法启动，这样创建进程比fork()还要简单。
# join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步。

## Pool
from multiprocessing import Pool
import time, random

def long_time_task(name):
	print('Run task %s (%s)...' % (name, os.getpid()))
	start = time.time()
	time.sleep(random.random() * 3)
	end = time.time()
	print('Task %s runs %0.2f seconds.' % (name, (end - start)))

if __name__ == '__main__':
	print('Parent process %s.' % os.getpid())
	p = Pool(4)
	for i in range(5):
		p.apply_async(long_time_task, args=(i,))
	print('Waiting for all subpeocess done...')
	p.close()
	p.join()
	print('All subprocess done.')

# 对Pool对象调用join()方法会等待所有子进程执行完毕，调用join()之前必须先调用close()，
# 调用close()之后就不能继续添加新的Process了

## 子进程
import subprocess

print('$ nslookup www.python.org')
r = subprocess.call(['nslookup', 'www.python.org'])
print('Exit code:', r)

# 如果子进程还需要输入，则可以通过communicate()方法输入：
print('$ nslookup')
p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
print(output.decode('utf-8'))
print('Exit code:', p.returncode)

## 进程间通信
from multiprocessing import Queue

# 写数据进程执行的代码
def write_p(q):
	print('Process to write: %s' % os.getpid())
	for value in ['A', 'B', 'C']:
		print('Put %s to queue...' % value)
		q.put(value)
		time.sleep(random.random() * 3)

# 读数据进程执行的代码
def read_p(q):
	print('Process to read: %s' % os.getpid())
	while True:
		value = q.get()
		print('Get %s from queue.' % value)

if __name__ == '__main__':
	# 父进程创建Queue 并传递给每个子进程
	q = Queue()
	pw = Process(target=write_p, args=(q,))
	pr = Process(target=read_p, args=(q,))
	# 启动子进程pw，写入:
	pw.start()
	# 启动子进程pr，读取:
	pr.start()
	# 等待pw结束:
	pw.join()
	# pr进程里是死循环，无法等待其结束，只能强行终止:
	pr.terminate()