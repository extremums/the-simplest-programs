# Funksiyalar mavzusi
# Faktarial sonni hisoblash dasturi
'''def factor(son):
    m=1
    for i in range(2,son+1):
        m*=i
    return m
son = int(input("Nechchi faktarial sonni chiqarishimni xohlaysiz  "))
a=factor(son)
print(a)'''
# Kvadrati kiritilgansondan sondan kichkina bo'lgan barcha sonlarni chiqar
"""def kichik_sonni_chiqarish(son):
    Kvadrati kiritilgan sondan kichkina 
    bo'lgan barcha sonlarni chiqarish dasturi
    kichik_son = 1  
    while kichik_son**2 < son :
        print(kichik_son**2)
        kichik_son+=1
son = int(input("Natural son kiriting "))
natija = kichik_sonni_chiqarish(son)
print(natija)"""
# a haqiqiy sonni k butun darajasini topish dasturi
'''from math import *    
while True :
        a=float(input("Son kiriting (haqiqiy yoki natural son bo'lish lozim)  "))
        b = input("Darajani kiriting(natural son kiritish lozim)  ")
        if b.isdigit() :
            c=pow(a,b)
            print(f"Kiritilgan {a}ning {b}-darajasi {c}ga teng  ")
        else:
            print("Natural son kiritish lozim  ")'''
# Uchta sondan kattasini topish dasturi
'''def max(a,b):
    if a>b:
        return a
    else:
        return b
def max3(a,b,c):
    return max(max(a,b),c)
a=int(input())
b=int(input())
c=int(input())
print(max3(a,b,c))'''
# tomoni n ga teng kvadrat chizish dasturi
'''def kvadrat_chiz(son):
    for i in range(1,son+1):
        print('*'*son,sep='\n')
son = input("n=")
if son.isdigit():
    son=int(son)    
    kvadrat_chiz(son)'''

# tomoni n ga teng kvadrat chizish dasturi(boshqacharoq yo'li)
'''def kvadrat_chizing(son):
    natija = 1
    while natija <= son:
        print('*'*son,sep='\n')
        natija += 1
son = input("n=")
if son.isdigit():
    son=int(son)    
    kvadrat_chizing(son)'''

# Kiritilgan sonning bo'luvchilarini chiqaruvchi dastur
'''def boluvchilarini_chiqar(son):
    for i in range(1,son+1):
        if son%i == 0:
            print(i,end=' ')
son = int(input("son kiriting  ")) 
boluvchilarini_chiqar(son)'''

# Kiritilgan sonni RIM raqamlarida ifodalovchi dasturi tuzing
'''a=[(1000,'M'),(900,"CM"),(500,'D'),(400,'CD'),(100,'C'),(90,'XC'),(50,"L"),(40,'XL'),(10,"X"),(9,'IX'),(5,'V'),(4,'IV'),(1,'I')]
def rim(n):
    s=''
    while n>0:
        for i,r in a:
            while n>=i:
                s+=r
                n-=i
    print(s)
while True:
    n=input("n ni kiriting ")
    if n.isdigit():
        n=int(n)
        rim(n)'''
# Kiritilgan sonni raqamlari yig'indisini topish dasturi
'''def raqamlari_yigindisi(son):
    a=0
    while son>0:
        a+=son%10
        son//=10
    print(a)
son = int(input("ihibui iujn "))
raqamlari_yigindisi(son)'''
# 5ta sondan eng kattasini va eng kichigini va qolgan 3 tasini orta arifmetigini chiqar
'''
def katta(a,b):
    if a>b:
        return a
    elif a<b:
        return b
    else:
        return a
def kattasi(a,b,c,d,e):
    return katta(katta(katta(a,b),katta(c,d)),e)


def kichik(a,b):
    if a>b:
        return b
    elif a<b:
        return a
    else:
        return a
def kichigi(a,b,c,d,e):
    return kichik(kichik(kichik(a,b),kichik(c,d)),e)


while True:
    a=list(input("Ballarni ortada boshliq tashlab kiriting ").split(" "))
    b = kattasi(a[0],a[1],a[2],a[3],a[4])
    c = kichigi(a[0],a[1],a[2],a[3],a[4])
    a.remove(b) ; a.remove(c) 
    d=(int(a[0])+int(a[1])+int(a[2]))/3
    print(f"Kiritilgan sonlarni eng kattasi {b} eng kichigi {c} o'rta arifmetigi  {d}")
'''

# Kiritilgan sonlarni so'zlarda chiqaruvchi dastur
'''a=[(50000,' ellik ming '),
(40000,' qirq  ming '),(30000,' o\'ttiz ming '),(20000,' yigrma  ming '),
(10000,' o\'n ming '),(9000,' to\'qqiz ming '),(8000,' sakkiz ming '),
(7000,' yetti ming '),(6000,' olti ming '),(5000,' besh ming '),
(4000,' to\'rt ming '),(3000,' uch ming '),(2000,' ikki ming '),
(1000,' ming '),(900,' to\'qqiz yuz '),(800," sakkiz yuz "),(700," yetti yuz "),
(600,' olti yuz '),(500,' besh yuz '),(400,' to\'rt yuz '),(300,' uch yuz '),
(200,'ikki yuz'),(100,' yuz '),(90,' to\'qson '),(80,' sakson '),(70,'yetmish'),
(60,' oltmish '),(50,' ellik '),(40,' qirq '),(30," o'ttiz "),(20," yigirma "),
(10," o'n "),(9," to'qqiz "),(8," sakkiz "),(7," yetti "),(6,' olti '),(5,' besh '),
(4,' to\'rt '),(3,' uch '),(2,' ikki '),(1,' bir ')]

def harf(son):
    while son>0:
        s=''
        for i,n in a:
            while son>=i:
                s+=n
                son-=i
        print(s)


son = int(input("Natural son kiriting (0 < a < 50000) shartni bajarishi lozim \n >>>"))
harf(son)'''

# Berilgan sonning raqamalari sonini aniqlash dasturi
'''def sonini(son):
    natija = 0
    while son>0:
        son//=10
        natija+=1
    return natija
while True:
    son=input("Natural son kiriting\n>>>")
    if son.isdigit():
        son=int(son)
        print(f"Kiritilgan sonning raqamlari {sonini(son)} ta")'''

# Yangi mavzu
'''b=100
def val():
    global b
    b=b-50
    print(b)
val()
print(b)
def val(d):
    print(d)
    d=100
    print(d)
d=200
val(d)'''

# S=1*5+2*6+3*7+...+n*(n+4) ni hisoblash dasturi
'''def hisobla(son):
    natija = 0
    for i in range(1,son+1):
        natija+=i*(i+4)
    print(natija)
n=int(input("Natural son kiriting\n>>>"))
hisobla(n)'''

# a,b,c sonlardan kattasini topish dasturi
'''a=int(input("birinchi sonni kiriting\n>>>"))
b=int(input("Ikkinchi sonni kiriting\n>>>"))
c=int(input("Uchinchi sonni kiriting\n>>>"))
def katta(a,b):
    if a>b:
        return a 
    else:
        return b
print(f"Kiritilgan sonlarning kattasi {katta(katta(a,b),c)} ga teng")'''

# Berilgan sonning EKUB ini hisoblash dasturi 
'''def ekub(a,b):
    while a!=0 and b!=0:
        if a>b:
            a%=b
        else:
            b%=a
    ekub_q=a+b
    return ekub_q
a=int(input())
b=int(input())
print(ekub(a,b))'''

# Berilgan 4 ta sonlardan eng kichigini topuvchi funksiya yarating
'''def min(a,b,c,d):
    if a>b:
        m=a
    elif a<b:
        m=b
    else:
        m=a
    if c>d:
        n=c
    elif c<d:
        n=d
    else:
        n=c
    if m>n:
        return m
    elif m<n:
        return n
    else:
        return m
        
a=list(input("4 ta butun son kiriting (boshidagi to'rtta sonni hisoblaydi)\n(bo'shliq tashlab kiriting )>>>").split(' '))
natija = min(int(a[0]),int(a[1]),int(a[2]),int(a[3]))
print(natija)'''

# Berilgan haqiqiy sonni k-darajaga ko'taruvchi funksiya 
'''def daraja(a,k):
    return a**k
a=float(input("Haqiqiy son kiriting\n>>>"))
k=int(input("Darajasini kiriting (butun son kiritish lozim)\n>>>"))
print(daraja(a, k))'''

# Inglizcha harf va raqamlardan iborat satrda nechta raqam borligini aniqlash dastur
'''def raqamlar(a):
    global s
    for i in a:
        if i=='1':
            s+=1
        elif i=='2':
            s+=1
        elif i=='3':
            s+=1
        elif i=='4':
            s+=1
        elif i=='5':
            s+=1
        elif i=='6':
            s+=1
        elif i=='7':
            s+=1
        elif i=='8':
            s+=1
        elif i=='9':
            s+=1
    print(s)
a=list(input("Matn kiriting  "))
s=0
raqamlar(a)'''

# Berilgan sonni akslantiruvchi (oxiri 0 bilan tugasa ham) dastur 
'''def akslantir(son):
    while son>0:
        s+=son%10
        son=son//10
    print(f"Kiritilgan sonning teskarisi \n>>> {s}")
son=int(input("Sonni kiriting\n>>> "))
akslantir(son)'''
 
# 0 bilan tugagan sonlarning raqamlari yig'indisini tsikl ishlatmagan holda hisobla
'''def raqam(son):
    if son==0:
        return 0
    else:
        return(son%10+raqam(son//10))

son=int(input("Natural son kiriting  "))
print(raqam(son))'''

# Listdagi o'xshash elementlar sonini aniqlash dasturi
'''a = [1,5,3,4,4,6,2,8,8,8,8,8]
b = len(a)
c = 1
for i in range(0,b):
    for n in range(i+1,b):
        if a[i]==a[n]:
            c+=1
            break
# Agar o'xshash elementlar yonma yon yozilgan bo'lsa break ni olib tashlash 
# lozim,bo'lmasa dastur xato ishlaydi
print(c)'''
















