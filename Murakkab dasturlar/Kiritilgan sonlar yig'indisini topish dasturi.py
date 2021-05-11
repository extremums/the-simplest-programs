# Kiritilgan sonlar yig'indisini topish dasturi
# append funksiyasini ishlashi
n = int(input("Massiv elementlar sonini kiriting  "))
a=[]
s=0
k=0
for i in range(n):
    a.append(int(input(f"a[{i}]= ")))
    if a[i]<0 :
        k+=1
        print("Manfiy son kiritilgani uchun sikl yakunlandi")
        break
    else:
        s+=a[i]
if k==0:
    print(f"Kiritilgan sonlarning yig'indisi {s}")
# append funksiyasini tarifi
'''a=['2005-yil']
a.append(input("Matn kiriting  ").split(' '))
print(a) ; print(a[0]) ; print((a[1])[0])'''
