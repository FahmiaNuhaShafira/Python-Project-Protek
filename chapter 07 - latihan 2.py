print('Latihan 2')
print()

namaFile = str(input('Masukkan nama file:' ))

try:
    selesai = False
    while not(selesai):
        menambahData= str(input('Data yang ditambahkan:'))
        file = open("E:/SEMESTER 1/Pemrograman terstruktur/Github/Python-Project-Protek/chapter 07 - contoh latihan", "a")
        file.write("(0)\n". format(menambahData))
        file.close()

        choice = None

        while choice not in("y", "n"):
            choice = str(input("Mau lagi (y/n):"))
            if(choice=='y'):
               selesai=False
            elif(choice=='n'):
                selesai=True
            else:
                print('Masukkan kembali pilihan (y/n)')

except FileNotFoundError:
    print('File tidak ditemukan')
