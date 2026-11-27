from itertools import *

# Буквы в алфавитном порядке
alph = sorted('цапля')

# Буквы не в алфавитном порядке
alph = sorted('цапля', reverse = True)

# Формирует все возможные комбинации с повторениями
for val in product('ФОКУС', repeat=5):
    val = ''.join(val)

for pos, val in enumerate(product('ФОКУС', repeat=5)):
    val = ''.join(val)

# Символы повторяются ровно 1 раз
eval(' and '.join(map(str, [val.count(i) == 1 for i in 'ПОБЕДА']))) or \
        sum(val.count(i) == 1 for i in 'ПОБЕДА') == 6 or \
        all(val.count(i) == 1 for i in 'ПОБЕДА') or \
        len(set(val)) == len(val)