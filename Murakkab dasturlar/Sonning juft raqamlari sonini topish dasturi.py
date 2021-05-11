# Sonning raqamlari yig'indisi,raqamlari soni va juft raqamlari sonini aniqlash
while True :
    n = input("Natural son kiriting  ")
    if n.isdigit() :
        n=int(n) ; b = 0 ; i=0 ; m=0 ; z = 0
        while n>=1:
            b= n%10
            n//=10
            m+=b
            z+=1
            if b != 0 and b%2 == 0:
                i+=1
        print(f"Kiritilgan sonning juft raqamlari {i} ta")
        print(f"Kiritilgan sonning raqamlari yig'indisi {m} ga teng .")
        print(f"Kiritilgan sonning raqamlari soni {z} ga teng .")
    else :
        print("Natural son kiritish lozim")
