# Kiritilgan sonning raqamlari yig'indisini aniqlash dasturi
while True :
    a=input("Natural son kiriting  ")
    if a.isdigit():
        a=int(a)
        b = 0
        c = 0
        while a>=1 :
            b+=a%10
            a = a//10
        print(b)
    else :
        print("Natural son kiritish lozim")
