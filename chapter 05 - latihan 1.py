print ("01")
indo = int(input('Nilai Bahasa Indonesia :'))
if(indo >= 0 and indo <= 100):

    mtk = int(input('Nilai Matematika :'))
if(mtk >= 0 and mtk <= 100):

    ipa = int(input('Nilai IPA:'))
if(ipa >= 0 and ipa <= 100):

    print('==========================')

if(indo>60 and ipa>60 and mtk>70):
    print ('LULUS')
else:
    print ('Tidak lulus')

print ("02")
indo = int(input('Nilai Bahasa Indonesia :'))
mtk = int(input('Nilai Matematika :'))
ipa = int(input('Nilai IPA:'))

print('==========================')

if(indo < 0 or indo > 100):
    print('Maaf input ada yang tidak valid')
elif(ipa < 0 or ipa > 100):
    print('Maaf input ada yang tidak valid')
elif (mtk < 0 or mtk > 100):
    print('Maaf input ada yang tidak valid')
    
elif(indo > 60 and ipa > 60 and mtk > 70):
    print ('Status kelulusan : Lulus')
else:
    print ('Status kelulusan : Tidak lulus')

print ("03")
indo = int(input('Nilai Bahasa Indonesia :'))
mtk = int(input('Nilai Matematika :'))
ipa = int(input('Nilai IPA:'))

print('==========================')

if(indo < 0 or indo > 100):
    print('Maaf input ada yang tidak valid')
elif(ipa < 0 or ipa > 100):
    print('Maaf input ada yang tidak valid')
elif (mtk < 0 or mtk > 100):
    print('Maaf input ada yang tidak valid')
    
elif(indo > 60 and ipa > 60 and mtk > 70):
    print ('Status kelulusan : Lulus')
else:
    print ('Status kelulusan : Tidak lulus')
    print('Sebab :')
    
    if(indo < 60):
        print('Nilai Bahasa Indonesia Kurang Dari 60')
    if(mtk < 70):
        print('Nilai Matematika Kurang Dari 70')

print ("04")
kodeKaryawan = int(input('Masukkan kode karyawan :'))
namaKaryawan = input('Masukkan nama karyawan :')
golongan = input('Masukkan golongan :')

print('====================================')

print('STRUK RINCIAN GAJI KARYAWAN')

print('-----------------------------------------------------------')

print('Nama Karyawan :' + namaKaryawan + '(Kode Karyawan :' + str(kodeKaryawan) + ')')
print('Golongan :' + golongan)

print('-----------------------------------------------------------')

if(golongan == 'A'):
    GajiPokok = 10000000
    Potongan = 2.5
    JumlahPotongan = 2.5 / 100 * 10000000
    GajiBersih = 10000000 - JumlahPotongan
elif(golongan == 'B'):
    GajiPokok = 8500000
    Potongan = 2.0
    JumlahPotongan = 2. / 100 * 8500000
    GajiBersih = 8500000 - JumlahPotongan
elif(golongan == 'C'):
    GajiPokok = 7000000
    Potongan = 1.5
    JumlahPotongan = 1.5 / 100 * 7000000
    GajiBersih = 10000000 - JumlahPotongan
elif(golongan == 'D'):
    GajiPokok = 5500000
    Potongan = 1.0
    JumlahPotongan = 1.0 / 100 * 5500000
    GajiBersih = 5500000 - JumlahPotongan
print('GajiPokok : Rp' + str(GajiPokok))
print('Potongan (' + str(Potongan) + '%): Rp' + str(JumlahPotongan))

print('-----------------------------------------------------------')

print('GajiBersih : Rp' + str(GajiBersih))

print ("05")
kodeKaryawan = int(input('Masukkan kode karyawan :'))
namaKaryawan = input('Masukkan nama karyawan :')
golongan = input('Masukkan golongan :')
status = input('Masukkan status (1: menikah, 2: blm) : ')
if(status == '1') :
    JumlahAnak = int(input('Masukkan Jumlah Anak :'))
    TunjanganMenikah = 10 / 100
    TunjanganAnak = 5 / 100 * JumlahAnak
    StatusMenikah = 'Sudah Menikah'
else:
    JumlahAnak = 0
    TunjanganMenikah = 0
    TunjanganAnak = 0
    StatusMenikah = 'Belum Menikah'

print('====================================')

print('STRUK RINCIAN GAJI KARYAWAN')

print('------------------------------------')

print('Nama Karyawan :' + namaKaryawan + '(Kode Karyawan :' + str(kodeKaryawan) + ')')
print('Golongan :' + golongan)
print('Status Menikah :' + StatusMenikah)
print('Jumlah Anak :' + str(JumlahAnak))

print('------------------------------------')

if(golongan == 'A'):
    GajiPokok = 10000000
    Potongan = 2.5
    JumlahTunjanganMenikah = 10000000 * TunjanganMenikah
    JumlahTunjanganAnak = 10000000 * TunjanganAnak
    GajiKotor = 10000000 + JumlahTunjanganMenikah + JumlahTunjanganAnak
    JumlahPotongan = 2.5 / 100 * GajiKotor
    GajiBersih = GajiKotor - JumlahPotongan
elif(golongan == 'B'):
    GajiPokok = 8500000
    Potongan = 2.0
    JumlahTunjanganMenikah = 8500000 * TunjanganMenikah
    JumlahTunjanganAnak = 8500000 * TunjanganAnak
    GajiKotor = 8500000 + JumlahTunjanganMenikah + JumlahTunjanganAnak
    JumlahPotongan = 2. / 100 * GajiKotor
    GajiBersih = GajiKotor - JumlahPotongan
elif(golongan == 'C'):
    GajiPokok = 7000000
    Potongan = 1.5
    JumlahTunjanganMenikah = 7000000 * TunjanganMenikah
    JumlahTunjanganAnak = 7000000 * TunjanganAnak
    GajiKotor = 10000000 + JumlahTunjanganMenikah + JumlahTunjanganAnak
    JumlahPotongan = 1.5 / 100 * GajiKotor
    GajiBersih = GajiKotor - JumlahPotongan
elif(golongan == 'D'):
    GajiPokok = 5500000
    Potongan = 1.0
    JumlahTunjanganMenikah = 5500000 * TunjanganMenikah
    JumlahTunjanganAnak = 5500000 * TunjanganAnak
    GajiKotor = 5500000 + JumlahTunjanganMenikah + JumlahTunjanganAnak
    JumlahPotongan = 1.0 / 100 * GajiKotor
    GajiBersih = GajiKotor - JumlahPotongan
print('Gaji Pokok : Rp' + str(GajiPokok))
print('Tunjangan Menikah : Rp' + str(JumlahTunjanganMenikah))
print('Tunjangan Anak : Rp' + str(JumlahTunjanganAnak))

print('------------------------------------')

print('Gaji Kotor : Rp' + str(GajiKotor))
print('Potongan (' + str(Potongan) + '%): Rp' + str(JumlahPotongan))

print('------------------------------------')

print('Gaji Bersih : Rp' + str(GajiBersih))
