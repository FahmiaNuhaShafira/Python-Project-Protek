print('-Python Project 10-')
print()

buah = {'apel' : 5000,
        'jeruk' : 8500,
        'mangga' : 7800,
        'duku' : 6500}

print("Daftar Buah")
number = 1
for x,y in buah.items():
    print("{0}. {1} : {2}".format(number,x,y))
    number += 1
total = 0
lagi = 'y'
while lagi == 'y':
    try:
        choose = input("Nama buah yang dibeli : ")
        if(choose in buah):
            kg = float(input('Berapa Kg             : '))
            total += (buah[choose] * kg)
            lagi = input("Beli buah yang lain (y/n) ? ")
        else:
            print('tidak ada dalam Daftar buah'.format(choose))
        
    except ValueError:
        print('Data Tidak Valid')

print('-'*20)
print("Total harga           :",total)
