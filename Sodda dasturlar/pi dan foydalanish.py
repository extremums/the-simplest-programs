import math
a=int(input("Kvadratning tomonini kiriting = "))
r=int(input("Kichik aylananing radiusini kiriting = "))
r1=a/2
s1=math.pi*r1**2
s2=math.pi*r**2
s=s1-s2
print(s)
