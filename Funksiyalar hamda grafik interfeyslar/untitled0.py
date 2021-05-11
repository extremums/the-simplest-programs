'''s=input().split(' ')
a=int(s[0])
k=int(s[1])
b=k/a
print(b)
a=input().split(' ')
b=int(a[1])/int(a[0])
print(b)'''
# z=int(input())
# c=0
# zz=z
# if z<0:
#     z=-1*z
# if z!=0:
#     for i in range(1,z+1):
#         if zz>0:
#             if zz%i==0:
#                 if i<=zz/i:
#                     c+=2
#         elif zz<0:
#             a=-1*zz
#             if a%i==0:
#                 if i**2==a:
#                     c+=2
#                 elif i<=a/i:
#                     c+=2
# else:
#     c=-1
# print(c)

# n=input().split('\n')
# M=list(n[0].split(' '))
# A=list(n[1].split(' '))
# S=int(M[1])
# b=len(A)
# s=0
# a=-1
# N=[]
# for i in range(0,b):
#     N.append(int(A[i]))
# while s<S:
#     s+=int(min(N))
#     N.remove(min(N))
#     a+=1
# print(a)

# s=input().split('\n')
# k=int(s[0])
# l=list(s[1])
# b=len(l)
# for i in range(0,b):
#     if l[i]=='a':
#         l[i]=='d'
#     elif l[i]=='b':
#         l[i]=='e'
#     elif l[i]=='c':
#         l[i]=='f'
#     elif l[i]=='d':
#         l[i]=='g'
#     elif l[i]=='e':
#         l[i]=='h'
#     elif l[i]=='f':
#         l[i]=='i'
#     elif l[i]=='g':
#         l[i]=='j'
#     elif l[i]=='h':
#         l[i]=='k'
#     elif l[i]=='i':
#         l[i]=='l'
#     elif l[i]=='j':
#         l[i]=='m'
#     elif l[i]=='k':
#         l[i]=='n'
#     elif l[i]=='l':
#         l[i]=='o'
#     elif l[i]=='m':
#         l[i]=='p'
#     elif l[i]=='n':
#         l[i]=='q'
#     elif l[i]=='o':
#         l[i]=='r'
#     elif l[i]=='p':
#         l[i]=='s'
#     elif l[i]=='q':
#         l[i]=='t'
#     elif l[i]=='r':
#         l[i]=='u'
#     elif l[i]=='s':
#         l[i]=='v'
#     elif l[i]=='t':
#         l[i]=='w'
#     elif l[i]=='u':
#         l[i]=='x'
#     elif l[i]=='v':
#         l[i]=='y'
#     elif l[i]=='w':
#         l[i]=='z'
#     elif l[i]=='x':
#         l[i]=='a'
#     elif l[i]=='y':
#         l[i]=='b'
#     elif l[i]=='z':
#         l[i]=='c'
# print(l)

# Rim shifrlash algaritmi

# a = [()]








# from math import*
# n=input().split(' ')
# n[0]=int(n[0])
# n[1]=int(n[1])
# n[2]=int(n[2])

# if abs(n[2]-n[0])<abs(n[2]-n[1]):
#     print('1-mushuk')
# elif abs(n[2]-n[0])>abs(n[2]-n[1]):
#     print('2-mushuk')
# else:
#     print('sichqon')



# m=input().split('\n')
# T=int(m[0])
# del m[0]
# for S in m:
#     b=len(list(S))
#     n=[]
#     j=[]
#     for i in range(1,b):
#         if int(S[i])!=int(S[i-1])+1:
#             break
#         if int(S[i])==int(S[i-1])+1:
#             print(f"YES {S[0]}")
    # for l in range(1,b):
    #      n.append(int(S[l])*10+int(S[l-1]))
    # w=len(n)
    # for q in range(1,w):
    #     if n[q]==n[q-1]+1:
    #         print(f'YES {n[0]}')
    # for o in range(2,b):
    #     j.append(int(S[o])*100+int(S[o-1])*10+int(S[0-2]))
    # f=len(j)
    # for t in range(1,f):
    #     if j[t]==j[t-1]+1:
    #         print(f"YES {j[0]}")


# dostlar = ['Davlat','Samandar',"Shahboz","Qahramon",'Aziz']
# n=0
# for dost in dostlar:
#     print(f"Salom {dost} bugun oshga borasanmi ?")
#     n+=1
# print(f"Kod {n} marta takrorlandi")

# for i in range(11,101,2):
#     print(i**3)

# # kino = []
# # print('5 ta eng sevimli kinolaringizni kiriting ')
# # for i in range(5):
# #     kino.append(input(f"{i+1}-sevimli kinoyingizni kiriting\n>>>"))
# # print(kino)
# dostlar = []
# soni = int(input("Nechi kishi bilan suhbatlashganingizni kiriting  "))
# for i in range(soni):
#     dostlar.append(input(f"{i+1}-suhbatlashgan odomingizni kiriting"))
# print(dostlar)


# yosh = int(input("Yoshingiz nechida?>>>"))
# if yosh>65: print("Siz COVID-19 risk guruhida ekansiz")


# x, y = 25, 50 # x=25 va y=50
# print("x>y") if x>y else print("x<y")

# cars=['toyota','mazda','hyundai','gm','kia']
# for car in cars :
#     if car!='gm':
#         print(car.upper())
#     else:
#         print(car.title())

# login = input("Iltimos loginingizni kiriting\n>>>")
# if login.lower()=='admin':
#     print("Xush kelibsiz admin foydalanuvchilar ro'yxatini ko'rasizmi ?")
# else:
#     print(f"Xush kelibsiz {login} !")

# son = float(input("Birinchi sonni kiriting "))
# son1 = float(input("Ikkinchi sonni kiriting "))
# if son==son1:
#     print("Sonlar teng")
# else:
#     print("Sonlar bir biriga teng emas")

# n=float(input("Son kiriting  "))
# if n<0:
#     print("Manfiy son")
# else:
#     print("Musbat son")

# son = float(input("Juft son kiriting: "))
# if son%2:
#     print('Bu son juft emas.')
# else:
#     print("Rahmat!")

# yosh = int(input("Yoshingizni kiriting  "))
# if yosh<4 or yosh>60:
#     print("Bepul")
# elif yosh<18:
#     print("10 000 so'm")
# else:
#     print("20000 so'm")    

# mahsulotlar = ['uzum','olma','anor','un','non','sut','musqaymoq','tarvuz','cola','fanta']
# savat = []
# soni = int(input("Nechta mahsulot olasiz"))
# for i in range(soni):
#     savat.append(input(f"{i+1}-mahsulot nomi ").lower())
# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         print(f"Do'konimizda {mahsulot} bor")
#     else:
#         print(f"Afsuski bizda {mahsulot} yo'q")

# mahsulotlar = ['uzum','olma','anor','un','non','sut','musqaymoq','tarvuz','cola','fanta']
# bor_mahsulotlar = []
# mavjud_emas = []
# mahsulot_soni = int(input("Nechta mahsulot olasiz ?  "))
# for i in range(mahsulot_soni):
#     mahsulot = input(f"{i+1}-mahsulotni kiriting  ")
#     if mahsulot.lower() in mahsulotlar:
#         bor_mahsulotlar.append(mahsulot)
#     else:
#         mavjud_emas.append(mahsulot)
# if not(mavjud_emas):
#     print("Do'konimizda hamma mahsulotlar bor ")
# else:
#     print("Do'konimizda quyidagi mahsulotlar yo'q")
#     for emas in mavjud_emas:
#         print(emas)

# foydalanuvchilar = ['anvar','nurullo','samandar','shahboz','aziz']
# login = input("Loginni kiriiting  ")
# if login.lower() in foydalanuvchilar:
#     print("Bu login band")
# else:
#     print("Xush kelibsiz")
#     foydalanuvchilar.append(login.title())

# son = int(input("Istalgan butun son kiriting   "))
# for i in range(2,11,2):
#     if son%i==0:
#         print(f"Kiritilgan son {i} soniga qoldiqiz bo'linadi")
# else:
#     print("Kiritilgan son 2 dan 10 gacha hech qaysi songa bo'linmaydi ")

son = int(input("Istalgan son kiriting: "))
if son>=0:print("Musbat son")
else:print("Manfiy son")


radius = 5
pi = 4.14 ; aylana_yuzi = pi*radius**2
print(aylana_yuzi)
























