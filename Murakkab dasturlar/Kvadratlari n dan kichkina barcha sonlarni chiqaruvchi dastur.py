# Kvadratlari n dan kichkina barcha sonlarni chiqaruvchi dastur
nurullo = True
while nurullo :
    n=input("(natural son kiritish lozim) n=")
    if n.isdigit() and n !=1 :
        n=int(n)
        a = 1
        nurullo = False
        while a**2 < n:
            print(a)
            a+=1
    elif n == 1 :
        print("1 dan kichkina natural son yo'q")
    else :
        print("Natural son kiritish lozim")
else :
    print("Dastur tugadi","Tamom",sep = '\n')
