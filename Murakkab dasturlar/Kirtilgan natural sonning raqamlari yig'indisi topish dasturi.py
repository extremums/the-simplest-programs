# Kirtilgan natural sonning raqamlari yig'indisi topish dasturi
nurullo = True
while nurullo :
    n=input("Natural son kiriting  ")
    if n.isdigit() :
        nurullo = False
        n= int(n)
        m = 0
        s = 0
        while n>=1:
            s+=n%10
            n = n//10
        print(f"Kiritilgan natular sonning raqamlari yi'gindisi {s} ga teng")
    else:
        print("Natural son kiritish lozim")
