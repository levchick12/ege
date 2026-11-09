from re import finditer

with open(r'../files/24_1975 (1).txt') as f:
    data =f.readline()
# data = 'P***P**PPP****P**P**P**PPP**P*P*P*P*P'

pattern = r'[QRS]*P([QRS]+P)+[QRS]*'

matches = [match.group() for match in finditer(pattern, data)]
print(len(max(matches, key=len)))