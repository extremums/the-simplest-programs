#Kiritilgan sonlar musbat va yig'indisi 100 katta bo'lsa nisbatini ,agar yig'indisi 100 kichik bo'lsa ko'paytmasini chiqaruvchi dastur
a=int(input("Birinchi sonni kiriting  "))
b=int(input("Ikkinchi sonni kiriting  "))
if a>0 and b>0 and a+b>100 :
    print(a/b)
elif a>0 and b>0 and a+b<100:
    print(a*b)
else :
    print("Kiritilgan ikki son shartni qanoatlantirmaydi")
