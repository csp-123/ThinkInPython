#!/usr/bin/env python3
# -*- coding: utf-8 -*-

## 进程间通信
from multiprocessing import Process, Queue
import os, time, random

# 写数据进程执行的代码
def write_p(q):
	print('Process to write: %s' % os.getpid())
	for value in ['A', 'B', 'C']:
		print('Put %s to queue...' % value)
		q.put(value)
		print(q.empty())
		time.sleep(random.random())

# 读数据进程执行的代码
def read_p(q):
	print('Process to read: %s' % os.getpid())
	a = 0
	while True:
		value = q.get()
		a = a + 1
		print('Get %s from queue.' % value)
		if a == 3:
			break

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
	# pr.terminate()