print('Praktikum 3.1')
print()

file = open("d:/data.txt", "r")
sum = 0
for data in file :
    sum = sum + int(data)
print(sum)
