print('-Python Project 04-')
print()

dataSayur = ['bayam','kangkung','wortel','selada']

#tambahsayur
def tambahSayur() :
    sayurTambahan = input('Nama sayur yang ingin ditambahkan :').lower()
    dataSayur.append(sayurTambahan)
    return dataSayur
#hapussayur
def hapusSayur() :
    sayurHapus = input('Nama sayur yang ingin dihapus :').lower()
    if(sayurHapus in dataSayur) :
        dataSayur.remove(sayurHapus)
    else :
        print('Sayur tersebut tidak ada dalam data')
    return dataSayur
#tampilkansayur
def readSayur() :
    print(dataSayur)

print('Menu:')
print('A. Tambah data sayur')
print('B. Hapus data sayur')
print('C. Tampilkan data sayur')
print('D. Selesai')

r = True
while(r == True) :
    print()
    opsi = input('Pilihan Anda :')
    if(opsi == 'A' or opsi == 'a') :
        tambahSayur()
    elif(opsi == 'B' or opsi == 'b') :
        hapusSayur()
    elif(opsi == 'C' or opsi == 'c') :
        readSayur()
    elif(opsi == 'D') :
        break
    else :
        print('Input tidak valid')
        continue
