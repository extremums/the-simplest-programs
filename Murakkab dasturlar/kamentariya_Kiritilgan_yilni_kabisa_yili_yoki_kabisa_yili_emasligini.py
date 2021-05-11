#Kiritilgan yilni kabisa yili yoki kabisa yili emasligini aniqlovchi dastur
kabisa = 'Kabisa yil 366 kun'
odatiy = 'Odatiy yil 365 kun'
yil = int(input('Yil kriting: '))
if yil % 4 != 0: 
    print(odatiy)
elif yil % 100 == 0:
    if yil % 400 == 0:
        print(kabisa)
    else:
        print(odatiy)
else:
    print(kabisa)
