print('Praktikum 2.1')
print()

#membuka dan mau membaca file E:/data.txt
file = open("c:/data.txt", "r")

#baca baris pertama dari file
#simpan ke dalam variabel bil1 sbg integer
bill = int(file.readline())

#baca baris pertama dari file
#simpan ke dalam variabel bil2 sbg integer
bill = int(file.readline())

#hitung dan tampilkan hasil bagi
hasil = bil1/bil2
print(bil1, 'dibagi', bil2, 'sama dengan', hasil)
