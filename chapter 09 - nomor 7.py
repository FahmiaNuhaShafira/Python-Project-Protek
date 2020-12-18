print('-07-')
print()

#data nama mahasiswa
mhs = ['K001:ROSIHAN ARI:1979-09-01:SOLO', 
       'K002:DWI AMALIA FITRIANI:1979-09-17:KUDUS',
       'K003:FAZA FAUZAN:2005-01-28:KARANGANYAR']

#tabel nilai
print ('=' * 61)
print ("NIM", "\tNAMA", "\t\t\t TGL LAHIR", "\t TEMPAT LAHIR")
print ('-' * 61)
for data in mhs :
    mhs1 = data.split(':')
    print (mhs1[0],"\t", end='')
    print (mhs1[1],"\t",end='')
    tgl = mhs1[2].split('-')
    tgl.reverse()
    tgl2 = '/'.join(tgl)
    if (len(mhs1[1])>11):
        print ("",tgl2,end='') 
    else :
        print ("\t",tgl2,end='')
    print ("\t",mhs1[3])
print ('-' * 61)
