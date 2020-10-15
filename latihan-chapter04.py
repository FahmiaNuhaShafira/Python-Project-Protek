print("01")
tarif1=200000
tarif2=10000
jammulai=6
menitmulai=0
jamselesai=23
menitselesai=50
waktusewa=(jamselesai-jammulai)+((menitselesai-menitmulai)//60)
sewa1=1
sewa2=waktusewa-12
totaltarif=sewa1*tarif1 + sewa2*tarif2
print("total tarif sewa = Rp ",totaltarif, ",00")

print("02")
jarak=795
bbm=12
bbmygdibutuhkan=jarak/bbm
print("Pak Budi memerlukan" ,bbmygdibutuhkan,"liter")

print("03")
kapasitas=50
isibensin=bbmygdibutuhkan//kapasitas
print("Pak Budi harus mengisi bensin minimal ",isibensin,"kali")

print("04")
jarakAB=125
V1=62
jarakBC=256
V2=70
mulai=6
istirahat=45/60
waktu1=jarakAB//V1
waktu2=jarakBC//V2
totalwaktu=(waktu1+waktu2)
sampaitujuan=mulai+totalwaktu
print("Pak Amir akan sampai di tempat tujuan pukul" ,sampaitujuan, ".00")

print("05")
laki = int(input("jumlah mahasiswa :"))
print("Laki-laki : ",'*' * 10,laki)
perempuan = int(input("jumlah mahasiswa perempuan :"))
print("Perempuan : ", '*' * 15,perempuan)
