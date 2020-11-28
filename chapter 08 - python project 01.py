print('-Python Project 01-')
print()

while True :
    try :
        n = int(input('Berapa banyak angka yang ingin diinput?'))
        break
    except ValueError :
        print('Input gagal/tidak valid')
        continue

DataInput= []
i = 0

while (i < n) :
    try :
        bil = int(input('Bilangan bulat yang diinginkan : '))
        DataInput.append(bil)
        i+= 1

    except ValueError :
        print("Input gagal/tidak valid")
        
DataInput.sort(reverse = True)
print(DataInput)

