print('-Python Pr0ject 09-')
print()

buah = { 'apel'  : 5000,
          'jeruk' : 8500,
          'mangga': 7800,
          'duku'  : 6500 }

#menghitung jumlah buah
def jumlahBuah():
    jumlah =int(input('Berapa Kg :'))
    print('-------------------------------')
    print('Total Harga            :',buah.get(namaBuah,0)*jumlah)

print('List Buah dan Harga ')

for x,y in buah.items() :
    print('.', x, ':', y)

while True :
    namaBuah = input('Nama buah yang dibeli :')
    if(namaBuah not in buah.keys()) :
        print('Buah yang dimaksud tidak ada')
        continue
    else :
        while True :
            try :
                jumlahBuah()
                break
            except ValueError :
                continue
        break
