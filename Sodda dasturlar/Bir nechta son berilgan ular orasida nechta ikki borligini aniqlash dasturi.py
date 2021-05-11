# Bir nechta son berilgan ular orasida nechta ikki borligini aniqlash dasturi
son = int(input("Nechta son kiritasiz  "))
a = [] ; k=1
for i in range(son):
    a.append(int(input(f"{i}-sonni kiritiing ")))
    while a[i] == 2:
        k+=1
        a[
