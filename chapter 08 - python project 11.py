print('-Python Project 11-')
print()

buah = { 'apel'  : 5000,
         'jeruk' : 8500,
         'mangga': 7800,
         'duku'  : 6500 }

def printDataBuah(databaseBuah):
    print('Data Buah')
    for i, j in databaseBuah.items():
        print('- {0} (Harga Rp{1} / kg)'.format(i,j))
        print('')

def checkOut(databaseBuah,namaBuah,banyakKilo):
    hargaBuah = databaseBuah.get(namaBuah)
    totalHarga = hargaBuah*banyakKilo
    return totalHarga

while True:
    print('Menu :\nA. Tambah data buah\nB. Beli buah\nC. Selesai')
    opsi = None
    
    while opsi not in('A','B','C'):
        opsi = str(input("Pilihan Menu: "))
        
        if(opsi == 'A'):
            printDataBuah(buah)
            namaBuahTambahan = str(input('Masukkan nama buah: '))

            if namaBuahTambahan in buah.keys():
                print('Nama buah telah terdaftar dalam database')
            else:
                while True:
                    try:
                        hargaBuahTambahan = int(input('Masukkan harga buah(dalam angka): '))
                    except ValueError:
                        print('Masukkan kembali dalam angka')
                        continue
                    else:
                        break
                buah[namaBuahTambahan] = hargaBuahTambahan
                print('{0} dengan harga {1} telah ditambahkan dalam database'.format(namaBuahTambahan,hargaBuahTambahan))
                print('')
                printDataBuah(buah)
                
        elif(opsi == 'B'):
            printDataBuah(buah)
            totalHarga = 0
            selesai = False
            
            while not(selesai):
                while True:
                    namaBuah = str(input('Nama buah yang dibeli              : '))
                    if(not(namaBuah in buah.keys())):
                        print('Nama buah tidak ditemukan')
                        continue
                    else:
                        break
                    
                while True:
                    try:
                        perkilo = float(input('Berapa kg (apabila desimal gunakan titik)   : '))
                    except ValueError:
                        print('Masukkan kembali dalam angka')
                        continue
                    else:
                        break
                    
                totalHarga = totalHarga + checkOut(buah,namaBuah,perkilo)
                opsi = None
                
                while opsi not in('y','n'):
                    opsi = str(input('Beli lagi (y/n)?: '))
                    if(opsi == 'y'):
                        selesai = False
                        print('')
                    elif(opsi == 'n'):
                        selesai = True
                    else:
                        print('Masukkan pilihan (y/n)')
                        
                print('------------------------------------------------')
                print('Total harga                              : {0}'.format(totalHarga))
                
        elif(opsi == 'C'):
            break

        else:
            print('Masukkan pilihan yang tersedia')
            continue
