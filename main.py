# def my_decorator(func):
#     def wrapper(arg):
#         print('Я - обертка!')
#         func(arg)
#         print('Завернули')
#     return wrapper
#
# @my_decorator
# def say_hello(name):
#     print(f'Hello, {name}')
#
# say_hello('Sam')

# x = ['5', '0', 9, 3, 2, 1, '9', 6, 7]
# y1 = 0
# z1 = 0
# y = list((map((lambda x: x if isinstance(x, int) else 0), x)))
# z = list((map((lambda x: int(x) if isinstance(x, str) else 0), x)))
# for i in range(len(y)):
#     y1+=y[i]
# for i in range(len(z)):
#     z1+=z[i]
# print(y1-z1)
string = 'hello world'
x = ''

# for i in range(len(string)):
#     if i < len(string)-1:
#         x += string[i] + ' '
#     else:
#         x += string[i]
# print(x)

# alphabet = [' ', '?', '!', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# arr = alphabet[::-1]
# for i in range(len(arr)):
#     arr += arr[i]
#     arr.
# print(*arr)
# import itertools
# laughing = 'HaHaHahahaHaHa'
# y = ''.join(c[0] for c in itertools.groupby(laughing.split('a')))
# # count = 0
# # for i in range(len(y)):
# #     if y[i] == 'H':
# #         count += 1
# #     elif y[i] == 'h':
# #         count += 1
# print(count)
# def mir(n, r=0):
#    return r if n == 0 else mir(n//10, r*10 + n % 10)
# lst = [102, 2, 85, 33, 14014]
# count = 0
# for i in range(len(lst)):
#    x = mir(*lst[i::-1])
#  #  print(x[0])
#  #  print(reversed(x[0]))
#    if lst[i] == x:
#         count += 1
#    else: count += 0
# print(count)

str = 'knife'
str1 = ''
str2 = list(str)
print(str2)
for i in range(len(str2)):
    if str2[i] != str2[i][::-1]:
        str1 = str.title()
    print(str1)
    print(str1)
