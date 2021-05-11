# n!/k!*(n-k)! ni hisoblash dasturi
# math moduli orqali ishlash
from math import *
n=int(input("(n>k ; n!=0 ; k!=0 shartlar bajarilishi lozim) n="))
k=int(input('(n>k ; n!=0 ; k!=0 shartlar bajarilishi lozim) k='))
if n>k and n!=0 and k!=0 :
    c = n-k
    a = factorial(n)
    b = factorial(k)
    d = factorial(c)
    n=a/(b*d)
    print(round(n))
else :
    print("n>k ; n!=0 ; k!=0 shart bajarilishi lozim")
# while va for operatori orqali ishlash
'''from math import *
n = int(input("(n>k ; n!=0 ; k!=0 shartlar bajarilishi lozim) n="))
k = int(input('(n>k ; n!=0 ; k!=0 shartlar bajarilishi lozim) k='))
if n>k and n!=0 and k!=0 :
    a=1; b=1; c=1; d=1; q=1; r=1; s=n-k
    while a<=n :
        b*=a
        a+=1
    while c <= k:
        d*=c
        c+=1
    while q <= s:
        r*=q
        q+=1
    w = b/(d*r)
    print(round(w))
else :
    print("n>k ; n!=0 ; k!=0 shartlar bajarilishi lozim")'''
# from random modulini tekshirish dasturi
'''from random import *
a = randint(1,50)
b = randint(1,50)
c=int(input(f"{a}+{b} = "))
if c == a+b :
    print("To'g'ri javob")
else :
    print("Noto'g'ri javob")'''
