# Berilgan sonning bo'luvchilarini chiqaruvchi dastur
while True :
    a=int(input("Natural son kiriting "))
    s = 0
    while s < a:
        s+=1
        if a%s == 0:
            print(s,end='  ')
    b = input("\nDastur davom etsinmi(ha/yoq)  ")
    if b=='ha' :
        continue
    else:
        break
