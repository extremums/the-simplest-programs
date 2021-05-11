# 1 dan songacha bo'lgan sonlarning oxirgi raqami 3 ga karralisini chiqarish
while True:
    a=input("Natural son kiriting  ")
    if a.isdigit():       
        a = int(a)
        b = 1 
        while b < a-1 :
            b+=1
            if b%10 == 3 or b%10 == 6 or b%10 == 9:
                print(b)
        break
    else:
        print("Narural son kiritish lozim")
print("Dastur tugadi\nTamom")
