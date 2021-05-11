# x ga karrali n ta sonni chiqaruvchi dastur
# Masalan: 8 ga karrali 6 sonni chiqar :0,8,16,24,32,40
son = input("Nechiga karrali sonni chiqarishni istaysiz  ")
karrali = input("Nechta chiqarishni xohlaysiz  ")
if son.isdigit() and karrali.isdigit() :
    son = int(son)
    karrali = int(karrali)
    for i in range(0,karrali):
        natija = i * son
        print('{} ga karrali son :{}'.format(son,  natija))
else :
    print("Son kiritish lozim")
