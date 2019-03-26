# dict 和 set
# Python内置了字典：dict的支持，dict全称dictionary，
# 在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度。

d = {'csp':95, 'ccp':85, 'ssp':75}
print(d['csp'])

# 如果key不存在，dict就会报错：
# 要避免key不存在的错误，有两种办法，一是通过in判断key是否存在：
print('ppp' in d)
# 二是通过dict提供的get()方法，如果key不存在，可以返回None，或者自己指定的value：
print(d.get('ppp'))

# 要删除一个key，用pop(key)方法，对应的value也会从dict中删除：
print(d.pop('ccp'))
print(d)

# set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，
# 所以，在set中，没有重复的key。
# 要创建一个set，需要提供一个list作为输入集合：
s = set([1,2,3,3])
print(s)

s.add(4)
print(s)

s.remove(4)
print(s)