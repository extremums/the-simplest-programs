# Kiritilgan matndagi so'zlarni sonini aniqlash dasturi
while True :
    a=input("Matnni kiriting  ")
    s = int(len(a))
    k = 0
    for i in range(s):
        if a[i] == ' ':
            k+=1
    print(f"Bu matnda {k+1} ta so'z bor")
