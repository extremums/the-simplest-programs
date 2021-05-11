#Kiritilgan uchta sondan musbat va manfiylar sonini aniqlash
a=int(input("Birinchi sonni kiriting "))
b=int(input("Ikkinchi sonni kiriting "))
c=int(input("Uchinchi sonni kiriting "))
k=0 ; d=0
if a>0:
    k+=1
else :
    d+=1
if b>0 :
    k+=1
else :
    d+=1
if c>0 :
    k+=1
else :
    d+=1
print(k,'ta son musbat',d,'ta son manfiy',sep=' ',end=' .')
