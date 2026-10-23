# s1 = set(input())
# s2 = set(input())
# if len(s1) >= len(s2):
#     print(s1)
# else:
#     print(s2)

fantasy_readers = {"Игорь", "Катя", "Лев", "Марина"}
detectve = {"Катя", "Лев", "Никита", "ольга"}
sci_fi = {"Лев", "Марина", "Никита", "Павел"}
s = fantasy_readers & detectve & sci_fi
s1 = fantasy_readers - detectve - sci_fi

