while True:
    a = int(input("Natural son kiriting  "))
    m = q = a ; k = 0 ; c = 0
    while a>=1:
        a//=10
        k+=1
    print(f"Kiritilgan son {k} xonali")
    while q>=1:
        c=c*10+(q%10)
        q//=10
    print(f"Kiritilgan sonning teskarisi {c}")
    if m==c :
        print("Kiritilgan son palendron son ")
    else:
        print("Palendron son emas ")