# Kiritilgan sonning hamma raqamlarini alohida qilib chiqarish dasturi
n = int(input("Natural son kiriting "))
a = 0 ; b = 0 ; p = n ;
while p>=1 :
    a = n%10
    p = p//10
for i in range(a,1,-1):
    while n >= 1 :
        m = n%10
        n //=10
        print(f"Kiritilgan sonning {i}-raqami {m}")
