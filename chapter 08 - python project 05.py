print('-Python Project 05-')
print()

def kuadrat(bil) :
    bilBulat = []
    for r in range(len(bil)) :
        perkalian = bil[r] * bil[r]
        bilBulat.append(perkalian)
    return bilBulat
bil = [2, 4, 5, 6]
hasil = kuadrat(bil)
print (hasil)
