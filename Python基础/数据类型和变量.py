# 数据类型
# 计算机顾名思义就是可以做数学计算的机器，因此，计算机程序理所当然地可以处理各种数值。但是，计算机能处理的远不止数值，还可以处理文本、图形、音频、视频、网页等各种各样的数据，不同的数据，需要定义不同的数据类型。在Python中，能够直接处理的数据类型有以下几种：
# 整数：
# Python可以处理任意大小的整数，当然包括负整数，在程序中的表示方法和数学上的写法一模一样，例如：1，100，-8080，0，等等。
# 计算机由于使用二进制，所以，有时候用十六进制表示整数比较方便，十六进制用0x前缀和0-9，a-f表示，例如：0xff00，0xa5b4c3d2，等等
# 对于很大的数，例如10000000000，很难数清楚0的个数。Python允许在数字中间以_分隔，因此，写成10_000_000_000和10000000000是完全一样的。十六进制数也可以写成0xa1b2_c3d4。
# 浮点数
# 浮点数也就是小数，之所以称为浮点数，是因为按照科学记数法表示时，一个浮点数的小数点位置是可变的，比如，1.23x109和12.3x108是完全相等的。浮点数可以用数学写法，如1.23，3.14，-9.01，等等。但是对于很大或很小的浮点数，就必须用科学计数法表示，把10用e替代，1.23x109就是1.23e9，或者12.3e8，0.000012可以写成1.2e-5，等等。
# 整数和浮点数在计算机内部存储的方式是不同的，整数运算永远是精确的（除法难道也是精确的？是的！），而浮点数运算则可能会有四舍五入的误差
# 字符串
# 字符串是以单引号'或双引号"括起来的任意文本，比如'abc'，"xyz"等等。请注意，''或""本身只是一种表示方式，不是字符串的一部分，因此，字符串'abc'只有a，b，c这3个字符。如果'本身也是一个字符，那就可以用""括起来，比如"I'm OK"包含的字符是I，'，m，空格，O，K这6个字符。
# 如果字符串内部既包含'又包含"怎么办？可以用转义字符\来标识，比如：

'I\'m \"OK\"!'

# 表示的字符串内容是：
# I'm "OK"!

# 转义字符\可以转义很多字符，比如\n表示换行，\t表示制表符，字符\本身也要转义，所以\\表示的字符就是\，可以在Python的交互式命令行用print()打印字符串看看：
print('i\'mok')

print('i\'myisgood\npython')

print('\\\n\\')

# 如果字符串里面有很多字符都需要转义，就需要加很多\，为了简化，Python还允许用r''表示''内部的字符串默认不转义，可以自己试试：

print('\\\n\\')

print(r'\\\t\\')

# 如果字符串内部有很多换行，用\n写在一行里不好阅读，为了简化，Python允许用'''...'''的格式表示多行内容，可以自己试试：
print('''...''')

print('''line1
... line2
... line3''')

# 上面是在交互式命令行内输入，注意在输入多行内容时，提示符由>>>变为...，提示你可以接着上一行输入，注意...是提示符，不是代码的一部分：
# 当输入完结束符```和括号)后，执行该语句并打印结果。
# 如果写成程序并存为.py文件，就是：

print('''
as1
as1
asd3
''')

# 多行字符串'''...'''还可以在前面加上r使用，请自行测试：
print(r'''hello,\n
world''')

# 布尔值
# 布尔值和布尔代数的表示方式完全一致，一个布尔值只有True，False两种值，要么True，要么是False。在python中，可以直接使用True False便是布尔值（需要注意大小写），也可以通过布尔值运算出来
True
False

print(5 > 10)
print(10 > 5)

# 布尔值可以使用and，or，not运算
# and运算是与运算，只有所有都为True，and运算结果才是True
print(1 < 2 and 3 > 2)

# or运算是或运算只是其中有一个为True,or运算结果就是True
print(3 > 1 or 4 > 5)

# not运算是非非运算，它是一个单目算符，把True变成False，False变成True
print(not False)
print(not True)
print(1 > 2, not False)

# 布尔值经常用在条件判断中，比如：
s = 10
if s >= 10:
    print('good')
else:
    print('no good')

# 空值
# 空值是Python里一个特殊的值，用None表示。None不能理解为0，因为0是有意义的，而None是一个特殊的空值。
# 此外，Python还提供了列表、字典等多种数据类型，还允许创建自定义数据类型，我们后面会继续讲到。

# 变量
# 变量的概念基本上和初中代数的方程变量是一致的，只是在计算机程序中，变量不仅可以是数字，还可以是任意数据类型。
# 变量在程序中就是用一个变量名表示了，变量名必须是大小写英文、数字和_的组合，且不能用数字开头，比如：
a = 1
# a 是一个整数

t_007 = 'T007'
# 变量t_007是一个字符串。

Answer = True
# 变量Answer是一个布尔值True。

# 在Python中，等号=是赋值语句，可以把任意数据类型赋值给变量，同一个变量可以反复赋值，而且可以是不同类型的变量，例如：
a = 123   # a 是整数
print(a)
a = 'abc' # a 是字符串
print(a)





