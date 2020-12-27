print('-02-')
print()

print ("Program Input Data Mahasiswa")
print ("Format : nim | nama mhs| alamat ")
print('-' *30)
print ("Data akan tersimpan dengan nama \"Data Mahasiswa.txt\" di folder yang sama")
file = open ("Data Mahasiswa.txt", 'a+')
status = True
while status == True :
    data = []
    nim = input ("\nNIM mahasiswa/i : ")
    data.append(nim)
    nama = input ("Nama mahasiswa/i : ")
    data.append(nama)
    alamat = input ("Alamat : ")
    data.append(alamat)
    gabung = ' | '.join(data)
    file.write(gabung + '\n')
    konfirmasi = input ("\nIngin menambahkan lagi? (y/n) : ")
    if konfirmasi != 'y' :
        print ("\nFile tersimpan")

        file.close()
        status = False
