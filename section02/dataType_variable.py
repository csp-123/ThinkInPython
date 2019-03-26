#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 数据类型和变量
print('''line1
line2
line3''')

# 字符串和编码
# 在最新的Python 3版本中，字符串是以Unicode编码
# 对于单个字符的编码，Python提供了ord()函数获取字符的整数表示，chr()函数把编码转换为对应的字符：
print(ord('A'))
print(ord('中'))
print(chr(66))
print(chr(25991))

print('ABC'.encode('ascii'))
print('中文'.encode('utf-8'))
print(b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore'))
print(len('ABC'))
print(len(b'\xe4\xb8\xad\xe6\x96\x87'))
print(len('中文'.encode('utf-8')))
print(len('中文'))


# 格式化 在Python中，采用的格式化方式和C语言是一致的，用%实现
print('Hello, %s' %'world')
print('Hi, %s, you have $%d.' %('csp', 100000000))

# 如果你不太确定应该用什么，%s永远起作用，它会把任何数据类型转换为字符串
print('Age: %s. Gender: %s' % (25, True))

# format()
print('Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125))
print()