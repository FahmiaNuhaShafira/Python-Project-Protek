print('-04-')
print()

#functionShuffleString(x,n)

import random
import sys
def shuffleString (kata, n):
    acak = []
    while (len(acak) < n):
        i = random.sample(kata, len(kata))
        hasil = ''.join(i)
        if hasil not in acak :
            acak.append(hasil)
    print (acak)
shuffleString('aku', 2)
shuffleString('aku', 3)
shuffleString('aku', 4)
