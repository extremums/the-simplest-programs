# Kiritilgan ma'lumot sonli bo'lsa dastur tugaydi aks holda qayta qayta ishlaydi
a = input(" Ma'lumot kiriting ")
while True :
    if a.isdigit():
        a = int(a)
        break
    print("Sonli ma'lumot kirtish lozim")
else :
    print("Dastur tugadi",'Tamom',sep='\n')
    
