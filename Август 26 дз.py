# Задание 1
a = list(input())
def max_streak(data, value):
    if value not in data:
        return "Значения нет"
    max_len = 0
    max_i = 0
    new_list = []
    for i in range(len(data)):
        if data[i] == value:
            new_list = []
        new_list.append(data[i])
    if len(new_list) > max_len:
        max_len = len(new_list)
        max_i = i
    return (max_len, max_i)
print(max_streak(a, '-'))