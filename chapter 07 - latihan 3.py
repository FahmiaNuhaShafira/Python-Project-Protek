print('Latihan 3')
print()
print('HITUNG RATA-RATA')
print('------------------------------')

masukkan=0
bagi=0
selesai=False

while not (selesai):
    try:
        menambahData = int(input('Masukkan bilangan bulat:'))
        masukkan = masukkan + menambahData
        bagi += 1
        choice = None
        while choice not in ("y","n"):
            choice = str(input('Lagi(y/n)?'))
            if(choice=='y'):
                selesai=False
            elif(choice=='n'):
                selesai=True
            else:
                print('Masukkan kembali pilihan (y/n)')

    except ValueError:
        print("Bukan bilangan bulat")

print('Rata-ratanya adalah : {0}'. format(masukkan/bagi))
