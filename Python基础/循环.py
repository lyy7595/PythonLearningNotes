# sum = 0
# for x in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
#     sum = sum + x
#     print(sum)
# #
# 如果要计算1-100的整数之和，从1写到100有点困难，幸好Python提供一个range()函数，可以生成一个整数序列，再通过list()函数可以转换为list。比如range(5)生成的序列是从0开始小于5的整数：
# a = 0
# for x in range(101):
#     a = a + x
#     print(a)

# names = ['Michael', 'Bob', 'Tracy']
# for name in names:
#     print(name)


# 第二种循环是while循环，只要条件满足，就不断循环，条件不满足时退出循环。比如我们要计算100以内所有奇数之和，可以用while循环实现：
# sum = 0
# n = 99
# while n > 0:
#     sum = sum + n
#     n = n - 2
#     print(sum)
# 请利用循环依次对list中的每个名字打印出Hello, xxx!：
# L = ['Bart', 'Lisa', 'Adam']
# for x in L:
#     print('hello', x, '!')
# n = 1
# while n <= 100:
#     if n > 10:
#         break
#     print(n)
#     n = n + 1
# print('end')

L = list(range(1001))

L.pop(0)#去掉1000以内的0，消除除以0的bug

L.pop(0)#去掉1000以内的1，消除所有数都不是质数的bug

re = []

for temp in L:

    result = True#作为是否为质数的标志

    for t in L:

        if(temp==t):#消除除以本身必定能整除的bug

            continue

        if(temp/t==temp//t):#整数除法和浮点数除法值相同说明temp可以被1000以内的值整除是非质数

            #print('{0}不是质数'.format(temp))

            result = False

            break

    if(result):

        re.append(temp)

        print('{0}是质数'.format(temp))

print('质数个数是：{0}'.format(len(re)))
