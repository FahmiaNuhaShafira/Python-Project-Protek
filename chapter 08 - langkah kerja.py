print('LANGKAH KERJA')
print('='*30)
print()


a = [1, 5, 6, 3, 6, 9, 11, 20, 12] 
b = [7, 4, 5, 6, 7, 1, 12, 5, 9]

#1
print('List awal a:\n', a)
print('List awal b:\n', b)
print('-'*30)

#2
a.insert(3,10)
b.insert(2,15)
print('List a setelah disisipkan nilai 10 ke indeks 3:\n',a)
print('List b setelah disisipkan nilai 15 ke indeks 2:\n',b)
print('-'*30)

#3
a.append(4)
b.append(8)
print('List a setelah disisipkan nilai 4 ke indeks terakhir:\n',a)
print('List b setelah disisipkan nilai 8 ke indeks terakhir:\n',b)
print('-'*30)

#4
a.sort()
b.sort()
print('List a setelah sorting secara ascending:\n',a)
print('List a setelah sorting secara ascending:\n',b)
print('-'*30)

#5
c=a[:8]
d=b[2:10]
print('List c yang elemennya merupakan sublist dari a(indeks 0-7):\n',c)
print('List d yang elemennya merupakan sublist dari b(indeks 2-9):\n',d)
print('-'*30)

#6
e=[]
for i in range(len(d)):
    e += [c[i]+d[i]]
print('List e yang elemennya merupakan hasil penjumlahan dari setiap elemen c dan d:\n',e)

#7
e=tuple(e)
print('List e yang dijadikan tuple:\n',e)
print('-'*30)

#8
min=min(e)
max=max(e)
sum=sum(e)
print('Min dari seluruh elemen e:\n',min)
print('Max dari seluruh elemen e:\n',max)
print('Sum dari seluruh elemen e:\n',sum)
print('-'*30)

#9
myString="python adalah bahasa pemrograman yang menyenangkan"
print('myString:\n',myString)

#10
myStringSet=set(myString)
print('Karakter huruf yang menyusun myString:\n',myStringSet)

#11
myStringSetList = list(myStringSet)
print('List myString\n',myStringSetList)
myStringSetList.sort()
print('List alfabet himpunan myString:\n',myStringSetList)





