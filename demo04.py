'''
字符串和编码
'''
# 'a' -> 97
# 'A' ->65
# ASCII America standard code for information interchange
# ord():获取字符的整数编码
print(ord('a'))
print(ord('旭'))
# chr():获取数字对应的字符
print(chr(25000))
# hex() 获取
print(hex(ord('中')))
print('\u4e2d')

# 进制转换
# 二进制 ，八进制 ，十六进制
a = 10
# bin(),十进制转二进制
print(bin(a))
# oct() 十进制转八进制
print(oct(a))
# hex() 十进制转十六进制
print(hex(a))
# int() 2,8,16 转 10进制
print(int(0b1010))

# 字符串长度
name = 'zxcv'
print(len(name))
# 字符串格式化
name =  input('请输入姓名')
age =int(input('请输入年龄'))
# %表示占位符 
# %s 字符串 在任何情况下都可以
# %d 整数
# %f 浮点数
# %x 十六进制 
print('我叫%s,今年%d岁' %(name,age))
percent =int(input('请输入值'))
print('我今年减肥了%d%%'%percent)
# format()
print('我叫{0},今年{1}岁， 我今年减肥了{2:.2f}%'.format(name,age,percent))
