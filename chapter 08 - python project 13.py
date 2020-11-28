print('-Python Project 13-')
print()

def nilaiTertinggi(nilaiMhs):
    nilaiX = 0
    
    for r in nilaiMhs:
        nilaiMID = r.get('mid')
        nilaiUAS = r.get('uas')
        nilaiAkhir = (nilaiMID + 2*nilaiUAS)/3
        
        if(nilaiAkhir > nilaiX):
            nilaiX = nilaiAkhir
            data = {}
            data['nim'] = r.get('nim')
            data['nama'] = r.get('nama')
    return data

nilaiMhs = [{'nim' : 'A01',
             'nama': 'Amir',
             'mid' : 50,
             'uas' : 80},
            {'nim' : 'A02',
             'nama': 'Budi',
             'mid' : 40,
             'uas' : 90},
            {'nim' : 'A03',
             'nama': 'Cici',
             'mid' : 50,
             'uas' : 50},
            {'nim' : 'A04',
             'nama': 'Dedi',
             'mid' : 20,
             'uas' : 30},
            {'nim' : 'A05',
             'nama': 'Fifi',
             'mid' : 70,
             'uas' : 40}]

nilaiTinggi = nilaiTertinggi(nilaiMhs)
print('nilai akhir tertinggi adalah {0} dengan NIM {1} '.format(nilaiTinggi['nama'], nilaiTinggi['nim']))
