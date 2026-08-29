# Задание 1
# a = list(input())
# def max_streak(data, value):
#     if value not in data:
#         return "Значения нет"
#     counter = 0
#     max_len = 0
#     max_i = 0
#     for i in range(len(data)-1):
#         if data[i] == value:
#             counter += 1
#             if counter > max_len:
#                 max_len = counter
#                 max_i = i
#             else:
#                 counter = 0
#     return (max_len, max_i - max_len + 1)
# print(max_streak(a, '-'))


# задача 2
# def to_binary(n, width = 8):
#     if n <= 0:
#         return 0
#     else:
#         a = bin(n)[2:]
#         if len(a) < width:
#             b = width - len(a)
#             d = "0" * b + a
#             return d
# print(to_binary(-5))


