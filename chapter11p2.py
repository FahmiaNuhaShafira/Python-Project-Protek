print('-02-')
print()

from datetime import *
import os

if(os.path.exists("dataPinjamanBuku.txt")) :
    fileMode = 'a'
else :
    fileMode = 'w'

file = open("dataPinjamanBuku.txt", fileMode)

while True :
    
    kode_member = input("Masukkan Kode Member : ")
    nama_member = input("Masukkan Nama Member : ")
    judul_buku = input("Masukkan Judul Buku : ")

    Tgl_pinjam = date.today()
    Tgl_kembali = Tgl_pinjam + timedelta(days = 7)

    dataPinjaman = [kode_member, nama_member, judul_buku, str(Tgl_pinjam), str(Tgl_kembali) + '\n']
    file.write('|'.join(dataPinjaman))

    ulangi = input("\nUlangi lagi (y/n) : ")

    if(ulangi.lower() == 'y') :
        continue
    
    elif(ulangi.lower() == 'n') :
        break

    else :
        print("Input tidak valid")
        break

file.close()
