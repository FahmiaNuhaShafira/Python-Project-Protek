print('-05-')
print()

nilai = [{'nim' : 'A01', 'nama' : 'Agustina', 'mid' : 50, 'uas' : 80},
         {'nim' : 'A02', 'nama' : 'Budi', 'mid' : 40, 'uas' : 90}, 
         {'nim' : 'A03', 'nama' : 'Chicha', 'mid' : 100, 'uas' : 50}, 
         {'nim' : 'A04', 'nama' : 'Donna', 'mid' : 20, 'uas' : 100},
         {'nim' : 'A05', 'nama' : 'Fatimah', 'mid' : 70, 'uas' : 100}]

#tabelnilai
print ('=' * 45)
print ("NIM", "\t NAMA", "\t\tN.MID", "\t\tN.UAS")
print ('-' * 45)
for data in nilai :
    print (data['nim'],"\t", end ='')
    if (len(data['nama']) > 6) :
        print (data['nama'],"\t", end ='')
    else :
        print (data['nama'],"\t\t", end='')
    print (data['mid'],"\t\t",end='')
    print (data['uas'])   
print ('-' * 45)
