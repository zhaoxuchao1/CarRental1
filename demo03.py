# 数据类型

# 整数 100
# 十六进制  0xabc0848c
# 浮点数 1.23
# 科学计数法：1.234e5 ，1.234e-5
#  \ 代表转义字符
print('\\') # \
print('\'') #'
print('i\'') #i'
# \n 换行  \t 制表符（作用是对齐）
print('你\n好')
print('你\t好')
print('你很\t好')
# r ：regular代表正常里面的转译字符无效
print(r'\\t\\') 
print('\\t\\')
# 打印多行
print('''你好
张三
该换钱了''')

'''布尔值 boolean'''
#True  False
print(True)
print(False)
print(3>2)
print(3==2)
# 布尔值可以进行逻辑运算
print(3>2 and 4<5)
print(3>2 or 3<2)
# 取反，逻辑非 单目运算符
print(not 3<4) # False

'''空值'''
#Nnoe
print(None)

'''变量'''
# 变量名必须是：大小写英文字母，数字或者'_'
a = 100
a1 = 200
a_2 = 200
# 2b = 300 #不能以数字开头
#见名知意
#驼峰命名法
teacherName = 'ckm'
#下划线命名法
teacher_first_name = 'fff'
a = 'zxc'
# 赋值
a = 33
print(a)
# 常量--名字中字母全部大写   是假常量
PI = 3.1425926
print(PI)