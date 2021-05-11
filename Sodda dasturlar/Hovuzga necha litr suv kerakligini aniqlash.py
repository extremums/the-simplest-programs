a=int(input("Hovuzning bo'yini kiritng(metrlarda ifodalang) = "))
b=int(input("Hovuzning enini kiritng(metrlarda ifodalang) = "))
h=int(input("Hovuzning chuqurligini kiritng(metrlarda ifodalang) = "))
c=a*h*2
d=b*h*2
e=a*b
f=c+d+e
g=(a*100)*(b*100)*(h*100)
i=g//1000
print("Hovuzni kafel bilan qoplash uchun ",f," metr kvadrat kafel kerak bo'ladi")
print("Hovuzni to'ldirish uchun ",i," litr suv kerak bo'ladi ")
