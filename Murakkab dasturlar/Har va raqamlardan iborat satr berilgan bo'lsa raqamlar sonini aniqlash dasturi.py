# Harf va raqamlardan iborat satr berilgan bo'lsa raqamlari sonini aniqlash dasturi
a = input("Matn kiriting  ")
k = 0
for i in a:
    if i.isdigit():
        k+=1
print(k)
