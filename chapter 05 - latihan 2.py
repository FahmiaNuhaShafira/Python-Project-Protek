print('01')
i=1
while (i <=100):
    print(i) 
    i=i + 2
print('02')
k=0
i=1
while (i <=100):
    print(i)
    i=i + 2
    k=k+1
print('Banyaknya bilangan ganjil : '+ str(k))
print('03')
k=0
i=1
sb=0
while (i <=100):
    print(i)
    sb= sb + i
    i=i + 2
    k=k+1
print('Banyaknya bilangan ganjil : '+ str(k))
print('Jumlah seluruh bilangan : ' + str(sb))
print('04')
kolom = 4
baris = 5

i = 0
while (i < baris) :
   j = 0
   while (j <= kolom) :
       print('* ', end='')
       j += 1
   print(' ')
   i += 1
   kolom -= 1
print('05')
print('Hai...nama saya mr, lappie, saya telah memilih sebuah bilangan bulat secara acak antara 0 s/d 100. Silahkan tebak ya!!!')
ta=int(input('Tebakan Anda : '))
while True:
    if(ta<10):
        print('Hehehe.....Bilangan tebakan anda terlalu kecil')
        ta=int(input('Tebakan Anda : '))
    elif(ta>10):
        print('Hehehe.....Bilangan tebakan anda terlalu besar')
        ta=int(input('Tebakan Anda : '))
    elif(ta==10):
        print('yeeee...Bilangan tebakan anda benar')
        break
print('06')
print('Hai...nama saya mr, lappie, saya telah memilih sebuah bilangan bulat secara acak antara 0 s/d 100. Silahkan tebak ya!!!')
ta=int(input('Tebakan Anda : '))
kurangpoin=0
while True:
    if(ta<10):
        print('Hehehe.....Bilangan tebakan anda terlalu kecil')
        ta=int(input('Tebakan Anda : '))
        kurangpoin+=2
    elif(ta>10):
        print('Hehehe.....Bilangan tebakan anda terlalu besar')
        ta=int(input('Tebakan Anda : '))
        kurangpoin+=2
    elif(ta==10):
        print('yeeee...Bilangan tebakan anda benar')
        score=100-kurangpoin
        print('Score anda : ' + str(score))
        break
