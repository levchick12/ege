# первая программа
# a = 10
# print(a)

# int - целочисленный тип данных
# float - дробный тип данных
# str - строка
# list - список
# tuple - кортеж
# set - множество уникальных значений
'''dict - словарик (множество ключевых значений)
ключ - это не все объекты
ключи уникальны между собой'''
# bool - логический тип
# name = 10 - int
# name1 = 10. - float
# name2 = "hello world" - str
# name3 = [1,2,3,4] - list
# name4 = (1,2,3,4,5,6) - tuple
# name5 = {1, 2, 2, 2, 2, 3, 4, 5, 6} - set
# name6 = {"hello":10}  - dict
# name7 = True - bool
# print(type(name), type(name1), type(name2), type(name3), type(name4), type(name5), type(name6), type(name7))

# + - / *
# // - целочисленное деление
# % - деление с состатком
# ** - степень
'''приоритетность:
() -1
** -2
 / * // % -3
 + - -4
 '''
# a = 9
# d = 10
# print(a * d)
# print(a / d) # при делении всегда float
# print(a // d)  # в меньшую сторону
# print(a % d)
# print(a ** d)

# неявные преобразования
# float > int > bool
# # print (a / d)

# string = int(input('Введи число:'))
# print(string, type(string))
'''int можно складывать с float, int, bool'''

# string = int(input())
# print(string)

# string1 = int(float(input()))
# print(string1)

''''' print(float('2.1')) # будет 2.1
 print(int('2.1')) # выдаст ошибку
 print(int(float('2.1'))) # выдаст 2'''

# num = int(10.2) # 10
# num = float(10) # 10.0
# num = list('10') # ['1', '0']
# num = set({}) # set()
# num = set([]) # set()
# num = set([1,1,1,2,3,55,7,6,6,6]) # {1, 2, 3, 6, 7, 55}
# num = tuple([1,2,3,4,4,5]) # (1, 2, 3, 4, 4, 5)
# num = bool() # False
# num = bool(0) # False
# num = bool(5) # True
# print(num)

