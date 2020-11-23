print ('Praktikum 2.2')
print()

try :
    file = open("E:/SEMESTER 1/Pemrograman terstruktur/Github/Python-Projects-Protek/data1.txt", "r")
    bil1 = int(file.readline())
    bil2 = int(file.readline())
    hasil = bil1/bil2
    
    print("{0} dibagi{1} sama dengan{2}".format(bil1,bil2,bil3))
    
except FileNotFoundError:
    print("file tidak ditemukan")

except ZeroDivisionError:
    print("tidak bisa deibagi dengan 0")
