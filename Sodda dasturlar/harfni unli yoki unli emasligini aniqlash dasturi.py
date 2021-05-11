# 1 dan 30 gacha sonlar kiritilganda harflarda chiqaruvchi dastur 
while True :
    a=input("Iltimos harf kiriting ")
    if a.isalpha() :
        if a=='a' or a=='e' or a=='i' or a=='o' or a=='u' or a=='o\'' or a=='o`' :
            print("Unli harf")
        else :
            print("Undosh harf")
    else :
        print("Harf kiritish lozim")

