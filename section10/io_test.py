## 文件读写
f = open('test.txt', 'r')
print(f.read())
f.close()

# Python引入了with语句来自动帮我们调用close()方法
with open('test.txt', 'r') as f:
	print(f.read())

# 如果文件很小，read()一次性读取最方便；如果不能确定文件大小，
# 反复调用read(size)比较保险；如果是配置文件，调用readlines()最方便
#for line in f.readlines():
#	print(line.strip()) # 把末尾的'\n'删掉

# 二进制文件
# 要读取二进制文件，比如图片、视频等等，用'rb'模式打开文件即可

# 字符编码
f = open('test.txt', 'r', encoding='utf-8', errors='ignore')
print(f.read())
f.close()

# 写文件
# 写文件和读文件是一样的，唯一区别是调用open()函数时，
# 传入标识符'w'或者'wb'表示写文本文件或写二进制文件
f = open('test1.txt', 'w')
f.write('Hello World')
f.close()

## StringIO
from io import StringIO
f = StringIO()
f.write('hello')
f.write(' ')
f.write('world!')

print(f.getvalue())

f = StringIO('Hello!\nHi!\nGoodbye!')
while True:
	s = f.readline()
	if s == '':
		break
	print(s.strip())

from io import BytesIO
f = BytesIO()
f.write('中文'.encode('utf-8'))
print(f.getvalue())

## 操作文件和目录
import os
print(os.name)

## 环境变量
# 在操作系统中定义的环境变量，全部保存在os.environ这个变量中

# 查看当前目录的绝对路径
print(os.path.abspath('.'))

# 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
print(os.path.join('E:\workspace\sublineWorkspace\ThinkInPython\section10', 'dirtest'))

# 然后创建一个目录
os.mkdir('E:\workspace\sublineWorkspace\ThinkInPython\section10\dirtest')

# 删掉一个目录
os.rmdir('E:\workspace\sublineWorkspace\ThinkInPython\section10\dirtest')

# 把两个路径合成一个时，不要直接拼字符串，而要通过os.path.join()函数，
# 这样可以正确处理不同操作系统的路径分隔符
# 同样的道理，要拆分路径时，也不要直接去拆字符串，而要通过os.path.split()函数，
# 这样可以把一个路径拆分为两部分，后一部分总是最后级别的目录或文件名
# os.path.splitext()可以直接让你得到文件扩展名，很多时候非常方便
# 对文件重命名:
os.rename('test.txt', 'test.py')
# 删掉文件:
os.remove('test.py')