#Nechta parta kerakligini aniqlovchi dastur
a=int(input("Birintchi guruhdagi o'quvchilari sonini kiriting - "))
b=int(input("Ikkinchi guruhdagi o'quvchilar sonini kiriting - "))
c=int(input("Uchinchi guruhdagi o'quvchilar sonini kiriting - "))
d=a+b+c
a1=d//2
a2=d%2
if a2>0 :
    a1=a1+1
else :
    a1=a1
print(a1," ta parta kerak bo'ladi .")
