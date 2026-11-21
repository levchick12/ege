with open(r'../files/24_17563.txt') as file:
    data = file.readline()
data = data.replace('*', "-")
data = data.replace('--',' ')
data = data.replace('-0', ' ')
while ' 0' in data:
    data = data.replace(' 0', ' ')
data = data.split()
print(len(max(data, key=len)))