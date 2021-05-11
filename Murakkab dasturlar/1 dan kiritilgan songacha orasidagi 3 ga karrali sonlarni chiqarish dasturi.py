# Kiritiilgan songacha bo'lgan sonlar orasidan 3 ga karralililarini chiqarish
# while usulida
'''while True:
    n =input("Natural son kiriting ")
    if n.isdigit():
        n = int(n) ; i = 0
        while i<n-1:
            i+=1
            if i%3==0:
                print(i)
        a=input("Dastur yana ishlasinmi (ha/yoq)  ")
        if a == 'ha':
            continue
        else :
            break
    else:
        print("Natural son kiritish lozim")'''
# for usuli
while True:
    n =input("Natural son kiriting ")
    if n.isdigit():
        n = int(n) ;
        for i in range(1,n):
            if i%3 == 0 :
                print(i)
        a=input("Dastur yana ishlasinmi (ha/yoq)  ")
        if a == 'ha':
            continue
        else :
            break
    else:
        print("Natural son kiritish lozim")
