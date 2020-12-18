print('-06-')
print()
nilai = [{'nim' : 'A01', 'nama' : 'Agustina', 'mid' : 50, 'uas' : 80},
         {'nim' : 'A02', 'nama' : 'Budi', 'mid' : 40, 'uas' : 90}, 
         {'nim' : 'A03', 'nama' : 'Chicha', 'mid' : 100, 'uas' : 50}, 
         {'nim' : 'A04', 'nama' : 'Donna', 'mid' : 20, 'uas' : 100},
         {'nim' : 'A05', 'nama' : 'Fatimah', 'mid' : 70, 'uas' : 100}]

#tabelnilai
print ('=' * 80)
print ("NIM", "\t NAMA", "\t\tN.MID", "\t\tN.UAS", "\t\tN.AKHIR", "\tSTATUS")
print ('-' * 80)
for data in nilai :
    print (data['nim'],"\t", end ='')
    if (len(data['nama']) > 6) :
        print (data['nama'],"\t", end ='')
    else :
        print (data['nama'],"\t\t", end='')
    print (data['mid'],"\t\t",end='')
    print (data['uas'],"\t\t", end='')
    nA = (data['mid'] + (2*data['uas']))/3
    nA_bulat = round(nA , 2)
    if (nA_bulat >= 60):
        status='LULUS'
    else :
        status='GAGAL'
    print (nA_bulat,"\t\t",status)
print ('-' * 80)
