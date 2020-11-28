print('-Python Project 08-')
print()

#data harga buah
buah = { 'apel'  : 5000,
          'jeruk' : 8500,
          'mangga': 7800,
          'duku'  : 6500 }

#rata-rata harga buah
def rerataHargaBuah(buah):
    totalHarga = 0
    jumlah = 0

    for r,y in buah.items():
        totalHarga += y
        jumlah += 1

    rerata = totalHarga/jumlah
    return rerata

def rerataHargaFruit(buah):
    harga = list(fruit.values())
    rata = sum(harga)/len(harga)
    return rerata

x = rerataHargaBuah(buah)
print('Rata-rata harga satuan dari seluruh buah yang ada adalah ',x)
