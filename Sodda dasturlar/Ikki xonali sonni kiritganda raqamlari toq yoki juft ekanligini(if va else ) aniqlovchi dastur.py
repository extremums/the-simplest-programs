#Ikki xonali sonni kiritganda raqamlari toq yoki juft(if va else) ekanligini aniqlovchi dastur
a=int(input("Iltimos ikki xonali son kiriting - "))
b=a%10 ; c=a//10
if c%2==0:
    a1='Sonning birinchi raqami juft'
else :
    a1='Sonning birinchi raqami toq'
if b%2==0:
    a2='Sonning ikkinchi raqami juft'
else :
    a2='Sonning ikkinchi raqami toq'
print(a1,a2)
