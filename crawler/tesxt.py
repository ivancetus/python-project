#[::-1] reverse order, [::2] del even numbers
# numbers = list(range(10))
# print(numbers)
# numbers = numbers[::-1]
# print(numbers)
# numbers = numbers[::2]
# print(numbers)

#
# numbers = [1, 2, 3, 4, 5]
# temp = numbers
# del temp[:]
# print(numbers, temp)

#
# a = int(input('Enter the first number: '))
# b = int(input('Enter the second number: '))
#
# a = a / b
# b = b // a
#
# print(f'a = {a}, b = {b}')


# try:
#     val = 10 / 0
#     print(val)
# except (ValueError, ZeroDivisionError):
#     print('ValueError or ZeroDivisionError exception raised...')
# except:
#     print('Something went wrong...')

#
# artists = ['Sting', 'Phil Collins', 'The Police', 'Queen', 'AC/DC']
# result = [len(artist) for artist in artists]
# print(result)

#
# items = list(('ball', 'pen', 'glass', 'book', 'pen', 'ball'))
# print(items)
# items = set(items)
# print(items)
# items = sorted(items)
# print(items)

#
# stocks = ['AMZN', 'TSLA', 'NVDA', 'AAPL', 'MSFT']
# ticker=""
# #a=[if ticker.startswith('A') ticker for ticker in stocks]
# b=[ticker for ticker in stocks if ticker.startswith('A')]
# c=[ticker for ticker in stocks if len(ticker) == 3]
# #d=[ticker if ticker.startswith('A') for ticker in stocks]
# e=[ticker for ticker in stocks if 'A' in ticker]
# print(b)
# print(c)
# print(e)

#
# next()
# iter()

#
# #list.insert(i, element)
# #=> put element in index[i] position,
# #if there were elements already exist, shift to the right
# numbers = list(range(4))
# for i in range(3):
#     numbers.insert(-1, numbers[i])
# print(numbers)

#
# course_name = 'python interview'
# del globals()['course_name']
# del course_name
#rm course_name
#remove course_name
# del(course_name)
# print(course_name)

#
# number = 10
# def change():
#     global number
#     number = 100
#     return number
# print(change())
# print(number)

#
# techs = tuple('pandas') + ('sql', )
# print(techs)

# #self-referencing list
# numbers = [1, 2, 3]
# numbers.append(numbers)
# print(numbers)
# print(numbers[3][3][3][3])

#
# #0%3==0
# i = 0
# while True and i <= 7:
#     if i % 3 == 0:
#         i += 1
#         continue
#     print(i, '#')
#     i += 1

# #zip()
# letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
# numbers = [1, 2, 3, 4, 5, 6, 7, 8]
# chessboard = [(i, j) for i, j in zip(letters, numbers)]
# print(chessboard)

#
# numbers = (10, 20, 30, 40, 50)
# numbers = numbers[-3:-2]
# print(numbers)
# numbers = numbers[-1] # from last element count 1 backword?
# print(numbers)

#
# coding = {1: 2, 2: 3, 3: 1}
# val = coding[2]
# for key in range(len(coding)):
#     val = coding[val]
# print(val)

#
# artists = ['Sting', 'Phil Collins', 'The Police', 'Queen', 'AC/DC']
# artists.pop()
# print(artists)

#
# number = 10
# def change():
#     number = 100
#     return number
# print(change())
# print(number)

#
# var = 10 % 3
# var = var == 1
# print(var)

# #list property
# a = [1, 2, 3, 4, 5]
# b = a
# b.pop()
# print(a)
# print(b)

#
# x,y=1,0
# try:
#     x/y
# except Exception as e:
#     print(e)

#
# stocks = ['AAPL', 'MSFT', 'NVDA', 'UBER']
# #stocks.append('TSLA')
# #stocks.extend(['TSLA'])
# #list.extend(stocks,['TSLA'])
# list.extend(stocks,'TSLA') #['AAPL', 'MSFT', 'NVDA', 'UBER', 'T', 'S', 'L', 'A']
# #list.append(stocks,'TSLA')
# print(stocks)

#
# numbers = [1, 2, 3, 4, 5]
# result = []
# idx=0
# for number in numbers:
#     result.append(numbers.pop())
#     idx+=1
#     print(f"loopCount: {idx}")
#     print(f"numbers: {numbers}")
#     print(f"result: {result}")
# print(result)

#
# x = 10 ** 2 + 10 / 2 + 10 // 5 + 13 % 5
# print(x)

#
# print(type(1e6))
# print(type(.0))
# print(type(0.))
# print(type(1))
# print(type(0))
# print(type(0.0))


# numbers = list(range(20))
# print(numbers[::2])
# print(numbers[::3])

#
# def func(number, result=[]):
#     result.append(number)
#     return result
# print(func(10))
# print(func(20))
# print(func(30))

#
# numbers = list(range(10))
# numbers[:5] = [sum(numbers[:5])] # 前四項被其總和取代
# print(numbers)

#
# try:
#     val = int(input('Enter a value: '))
#     print(val / len(val))
# except ZeroDivisionError:
#     print('ZeroDivisionError raised...')
# except: # TypeError
#     print('Bad input...')

#
# ds_techs = ('sql', ) + ('pandas', )
# dev_techs = ('git', ) + ('aws', )
# techs = ds_techs + dev_techs
# print(techs)

#
# net_profit = [-10.5, 4.5, 30.8, -3.5, 14.0]
# #a=[value for value in net_profit if value>=0 else 0]
# #b=[value for value in net_profit else 0]
# c=[value if value>=0 else 0 for value in net_profit]
# d=[value if value>=0 else abs(value) for value in net_profit]

# set(dict) => only keys will be put into the set
# d={1:2,2:3,3:4}
# a=set(d)
# print(a)

# #deep copy vs shallow copy
# stocks = [['AAPL', 'MSFT'], ['AMZN', 'TSLA', 'NVDA']]
# import copy
# stocks_copy1=copy.copy(stocks)
# stocks_copy2=copy.deepcopy(stocks)
# stocks_copy3=list.copy(stocks)
# stocks_copy4=stocks.copy()

# all() / any()
# We need to check if at least one element of the iterable object
# evaluates to the truth. What built-in function can you use for this?

# incorrect way to remove even numbers in a list
# numbers = [1, 2, 3, 4, 5, 6, 7, 8]
# for i in numbers:
#     if i % 2 != 0 and i < len(numbers):
#         del numbers[i]
# print(numbers)

# numbers = [1, 2, 3, 4, 5, 6, 7, 8]
# for i in numbers[:]: # Iterating over the copy of the list
#     if i % 2 != 0 and i < len(numbers):
#         del numbers[i]

# # use the following instead
# for i in numbers:
#     if i%2==0:
#         numbers.remove(i)
# print(numbers)

#
# a = [1, 2, 3, 4, 5]
# b = a
# b[:] = [3, 6]
# print(a)
# print(b)

