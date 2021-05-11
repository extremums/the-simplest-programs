# Palendron sonlarni aniqlash dasturi
nurullo = True
while nurullo :
    n = input("Natural son kiriting ")
    if n.isdigit():
        n: int=int(n)
        p = 0
        q = n
        m = n
        s = 0
        while n>=1:
            n = n/10
            s+=1
        print(f"Kirtilgan son {s} xonali")
        while m>=1:
            p=p*10+m%10
            m = m//10
        print("Bu sonning teskarisi= ",p)
        if p == q :
            print("Kiritilgan son palendron son")
        else:
            print("Kiritilgan son palendron son emas")
    else :
        print("Natural son kiritish lozim")
