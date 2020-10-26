print ("-01-")
i = 0
while(i < 10):
    print('Hello World')
    i += 1
print ("-05-")
i = 2
while (i<=20):
    print ('Hello World')
    i +=2
print("-06-")
i = 0
while True:
    print('Hello World')
    i += 1
    if (i==10):
        break
print("-08-")
#kotak bintang ajaib
kolom = 5
baris = 5

i = 0
while (i<baris):
    j=0
    while(j<kolom):
        print('* ', end='')
        j+=1
    print('')
    i += 1
print("-10-")
kolom = 0
baris = 5
i = 0
while (i<baris):
    j=0
    while(j<=kolom):
        print('*', end='')
        j += 1
    print('')
    i += 1
    kolom += 1
print("-11-")
from random import randint
while True:
    bil = randint(0, 10)
    print(bil)
    if bil == 5:
        break
print("-13-")
from random import randint
sum = 0
while True:
    bil = randint(0, 10)
    print(bil)
    sum = sum + 1
    if bil == 5:
        break
print('Jumlah Perulangan : ' + str(sum))
