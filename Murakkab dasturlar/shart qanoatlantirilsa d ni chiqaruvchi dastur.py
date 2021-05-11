# n >= 2 shartni qanoatlantirsa d = 1*2+2*3+..+(n-1)*n ni chiqaruvchi dastur
d = 0 
n=int(input("n = "))
if n >= 2 :
    for i in range(1,n) :
        d = d+i*(i+1)
    print(d)
else :
    print("Kiritilgan son berilgan shartni qanoatlantirmada ")
