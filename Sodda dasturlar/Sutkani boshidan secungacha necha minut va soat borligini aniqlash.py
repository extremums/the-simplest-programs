# Sutkani boshidan secungacha necha minut va soat borligini aniqlash
sekund = input("Sekundni kiriting  ")
if sekund.isdigit():
    sekund = int(sekund)
    soat = sekund//3600
    sekund %= 3600
    minut = sekund//60
    sekund %= 60 
    print("Sutkani boshidan {} soat {} minut va {} secund o'tdi".format(soat,minut,sekund))
else :
    print('Natural son kiritish lozim')
