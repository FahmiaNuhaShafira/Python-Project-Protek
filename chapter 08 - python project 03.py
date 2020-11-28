print('-Python Project 03-')
print()

try:
    count = int(input('Berapa mahasiswa yang ingin diinput? '))
    loop = 0
    data = []
    while loop < count:
        namaMahasiswa = input("Nama mahasiswa ke-{0} : ".format(loop+1))
        data.append(namaMahasiswa)
        loop += 1
    data.sort()
    print('-'*10, 'Hasil', '-'*10)
    for namaMahasiswa in data:
        print("{0} ({1} karakter)".format(namaMahasiswa,len(tuple(namaMahasiswa))))        
except ValueError:
    print('Data Tidak Valid')
