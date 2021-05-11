#Ikki xonali sonni (if va elif)kiritganda raqamlari toq yoki juft ekanligini aniqlovchi dastur
a=int(input("Iltimos ikki xonali son kiriting - "))
c=a//10 ; b=a%10
if c%2==0:
    a1='Sonning birinchi raqami juft'
elif c%2==1:
    a1='Sonning birinchi raqami toq'
if b%2==0:
    a2='Sonning ikkinchi raqami juft'
elif b%2==1 :
    a2='Sonning ikkinchi raqami toq'
print(a1,a2)
