#1 dan n gacha bo'lgan sonlar kvadratlarini yig'indisini topuvchi dastur
n=input("Nechchigacha kvadratlarini yig'indisini hisoblab bersin(o'sha sonni o'zi kirmaydi) ")
natija = 0
if n.isdigit():
    n = int(n)
    for i in range(n):
        kvadrati = i**2
        natija += kvadrati
    print('1 dan {} gacha bo\'lgan sonlar kvadratini yig\'indisi  {}'.format(n,natija))
else :
    print("Butun musbat son kiritish lozim")
