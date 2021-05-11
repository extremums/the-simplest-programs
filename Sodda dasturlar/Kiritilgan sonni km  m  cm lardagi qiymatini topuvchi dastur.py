a=int(input("Uzunlik kiriting(millimetrlarda ifodalang) = "))
b=a//1000000
a=a%1000000
c=a//1000
a=a%1000
d=a//10
a=a%10
print(b," km ",c," m ",d," cm ",a," mm")
