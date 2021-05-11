a=int(input("Sekundni kiriting = "))
b=a//3600
a=a%3600
d=a//60
a=a%60
print(b," soat ",d," minut ",a,"sekund")
