## asyncio 异步IO
# asyncio的编程模型就是一个消息循环。我们从asyncio模块中直接获取一个EventLoop的引用，
# 然后把需要执行的协程扔到EventLoop中执行，就实现了异步IO。
import asyncio

@asyncio.coroutine
def hello():
	print('Hello world!')
	# 异步调用asyncio.sleep(1)
	r = yield from asyncio.sleep(1)
	print('Hello again!')

# 获取EventLoop
loop = asyncio.get_event_loop()
# 执行 coroutine
loop.run_until_complete(hello())
loop.close()


import threading

@asyncio.coroutine
def hello1():
	print('Hello world! (%s)' % threading.currentThread())
	yield from asyncio.sleep(1)
	print('Hello again! (%s)' % threading.currentThread())

loop1 = asyncio.get_event_loop()
tasks = [hello1(), hello1()]
loop1.run_until_complete(asyncio.wait(tasks))
loop1.close()


@asyncio.coroutine
def wget(host):
	print('wget %s...' % host)
	connect = asyncio.open_connection(host, 80)
	reader, writer = yield from connect
	header =  'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
	writer.write(header.encode('utf-8'))
	yield from writer.drain()
	while True:
		line = yield from reader.readline()
		if line == b'\r\n':
			break
		print('%s header > %s' % (host, line.decode('utf-8').rstrip()))

	writer.close()

loop = asyncio.get_event_loop()
tasks = [wget(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()


## async/await
@asyncio.coroutine
def hello():
	print("Hello world!")
	r = yield from asyncio.sleep(1)
	print("Hello again!")

# 新语法
async def hello():
	print("Hello world!")
	r = await asyncio.sleep(1)
	print("Hello again!")

