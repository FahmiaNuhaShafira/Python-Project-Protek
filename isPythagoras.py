print('01')
def isPythagoras (a,b,c):
    if((a*a)==(c*c)-(b*b) or (b*b)==(c*c)-(a*a) or (c*c)==(a*a)+(b*b)):
        print(True)
    else:
        print(False)

print('1a')
isPythagoras(3,4,5)
print('1b')
isPythagoras(5,9,12)
print('1c')
isPythagoras(8,6,10)
print('1d')
isPythagoras(7,8,11)
