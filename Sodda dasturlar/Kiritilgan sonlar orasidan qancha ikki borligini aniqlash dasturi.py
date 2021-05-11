# Kiritilgan sonlar orasidan qancha ikki raqami borligini aniqlash dasturi
n = int(input("Massiv elementlar sonini kiriting  "))
a=[] ; k =0 ; z = 0
for i in range(n):
    a.append(int(input(f'son[{i}] = ')))
    while a[i]>=1 :
        k=a[i]%10
        a[i] = a[i]//10
        if k==2 :
            z+=1
print(z)
        
