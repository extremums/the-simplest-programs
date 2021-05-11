# a dan b gacha bo'lgan juft sonlarni chiqaruvchi dastur
a = int(input("(a <= b shartni bajarishi lozim) a= "))
b = int(input("(a <= b shartni bajarishi lozim) b= "))
if a%2==1:
    a+=1
    if a<b :
        for i in range(a,b,2):
            print(i)
    elif a==b :
        print("a dab b gacha sonlar mavjud emas")
    else :
        print(" a<=b shart bajarilishi lozim")
else :
    if a<b :
        for i in range(a,b,2):
            print(i)
    elif a==b :
        print("a dab b gacha sonlar mavjud emas")
    else :
        print(" a<=b shart bajarilishi lozim")
