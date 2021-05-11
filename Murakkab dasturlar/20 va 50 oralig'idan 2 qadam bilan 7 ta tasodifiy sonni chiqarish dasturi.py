# 20 va 50 oralig'idan 2 qadam bilan 7 ta tasodifiy sonni chiqarish dasturi
from random import *
a=[]
for i in range(7):
    a.append(i)
    a[i] = randrange(20,50,2)
    print(f'a[{i}] = ',a[i])
