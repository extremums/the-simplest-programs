# Kiritilgan sonning raqamlari sonini aniqlash dasturi
while True:
    a=input("Natural son kiriting  ")
    if a.isdigit():
        a=int(a)
        b = 0
        c = 0
        while a>=1:
            b+=a%10
            a=a//10
            c+=1
        print(c)
        break
    else:
        print("Natiral son kiritish lozim")
