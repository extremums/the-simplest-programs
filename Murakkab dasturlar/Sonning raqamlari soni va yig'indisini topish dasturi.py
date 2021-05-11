# Kiritilgan sonning raqamlari yig'indisini va sonini topish dasturi
while True :
    a =input("Natural son kiriting  ")
    if a.isdigit() :
        a = int(a); b = 0; c = 0
        while a >= 1 :
            b+=a%10
            a//=10
            c+=1
        print(f"Kiritilgan sonning raqamlari soni {c} ga teng")
        print(f"Raqamlari yig'indisi esa {b} ga teng")
    else :
        print("Natural son kiritish lozim")
