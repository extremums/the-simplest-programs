# import random modulining randint funksiyasi haqida
# Ikki sonni qo'shib chiqarganda tekshiruvchi dastur
while True :
    import random
    a=random.randint(6,10)
    b=random.randint(6,10)
    c=int(input(f"{a}*{b} = "))
    if c==a*b:
        print("To'g'ri")
    else:
        print("Noto'g'ri")
