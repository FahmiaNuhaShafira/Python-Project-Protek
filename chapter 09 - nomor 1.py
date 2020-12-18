print ('-01-')
print ()

#ubahHuruf

def ubahHuruf(teks, a, b) :
    listTeks = list(teks)
    hasilTeks = ''
    for char in listTeks :
        if(char == a) :
            char = b
        hasilTeks = ''.join([hasilTeks,char])
    return hasilTeks
print(ubahHuruf('MATEMATIKA', 'T', 'S'))
