print('-Python Project 06-')
print()

def sortStringByChar(myData) :
    myData.sort(reverse = True)
    return myData
myData = ['apel','rambutan','jeruk']
dataBaruSorted = sortStringByChar(myData)

print('Data list yang baru :', dataBaruSorted)

