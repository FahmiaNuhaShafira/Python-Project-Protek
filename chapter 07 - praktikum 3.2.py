print ('praktikum 3.2')
print()

try :
    file = open("E:/SEMESTER1/Pemrograman terstruktur/Github/Python-Projects-Protek/data2.txt", "r")
    sum = 0
    for data in file :

        try :
            sum = sum + int(data)
            print(sum)

        except ValueError:
            print('Tipe data tidak valid')

except FileNotFoundError :
    print('File tidak ditemukan')
