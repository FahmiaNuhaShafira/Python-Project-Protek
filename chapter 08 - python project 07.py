print('-Pyhton Project 07-')
print()

#data buah
buah = { 'apel'  : 5000,
         'jeruk' : 8500,
         'mangga': 7800,
         'duku'  : 6500 }

def mostExpensive(dictionary) :
    
    key = list(dictionary.keys())
    values = tuple(dictionary.values())
    hargaExpensive = max(values)
    indexHargaExpensive = values.index(hargaExpensive)
    print(key[indexHargaExpensive])

#hasil: buah dengan harga paling mahal
print('buah yang harga satuannya paling mahal:')
mostExpensive(buah)
