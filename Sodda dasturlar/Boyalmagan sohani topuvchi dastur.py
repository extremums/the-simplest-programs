#Kvadrat ichidagi aylanani tashqarisi ya'ni bo'yalmagan sohani topuvchi dastur
import math
a=int(input("Kvadrat tomonini kiriting - "))
r=int(input("Kichkina aylanani radiusini kiriting"))
a1=a/2
S=math.pi*r**2
S1=math.pi*a1**2
b=S-S1
print("Boyalmagan soha",b,sep=' ',end='.')
