'''
列表 list
'''

# 定义列表 ，列表中的每一个数据是一个元素
names = ['徐美斌','白宝蕾','陈杏梅','党海斌','冯凯']
print(names)
# 获取列表的长度

length = len(names)
print('length=%d'%length)

# 按照下标获取列表元素
print(names[1])

# 获取列表的最后的一位元素
print(names[-1])
print(names[-2])

# 添加元素 append：追加
names.append('高换')

# 插入
# names.insert(1,'郭金凤')
names.insert(1,'郭金凤')
print(names)

# 删除 pop() 删除最后一个元素,并返回该元素的值 
classmate1 = names.pop()
print(names)
print(classmate1)
# 删除指定的下标元素，并返回该元素的值
classmate2 = names.pop(0)
print(names)
print(classmate2)

# 替换（修改）  替换索引下的元素
names[0] = '陆凯丽'
print(names)
# spilt 切割方法，以's'来进行分割，切割后s不存在，其余的在类表中以字符串存在
f = 'ksldkaks jsdkajdk'
n = f.split('s')
print(n)

names.append(9527)
print(names)
# 列表的元素可以是另一个列表
names.append([True,False])
print(names)
# 获取列表里的列表元素 
print(names[6][0])

# 空列表
j = []
print(j) 
price =float(input('请输入单价(￥)'))
number =float(input('请输入数量（￥）'))
money = float(input('请输入金额（￥）'))
receivable = float(price * number)
change = float(money - receivable)
print('应收金额%f 找零%f'%(receivable,change))
# print('price{1:.1f},number{2:.1f},number{3:.1f},应收金额{4:.1f}找零{5:.1f}'.format(price,number,money,receivable,change))

