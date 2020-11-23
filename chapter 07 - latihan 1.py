print('Latihan 1')
print()

namaFile = str(input("Masukkan nama file: "))

try:
    file = open("E:/SEMESTER 1/Pemrograman terstruktur/Github/Python-Project-Protek/chapter 07 - contoh latihan.txt", "r")
    print(file.read())

except FileNotFoundError:
    print('File tidak ditemukan')
