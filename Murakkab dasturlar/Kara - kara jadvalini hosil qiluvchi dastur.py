# Karra jadvalini hosil qiluvchi dastur
karra = input("Nechi karrani hosil qilmoqchisiz  ")
if karra.isdigit():
    karra = int(karra)
    for son in range(1,11):
        natija = karra*son
        print('{} * {} = {}'.format(karra,son,natija))
else :
    print("Son kiritish lozim")
