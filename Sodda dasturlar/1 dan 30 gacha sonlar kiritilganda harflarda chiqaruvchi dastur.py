# 1 dan 30 gacha sonlar kiritilganda harflarda chiqaruvchi dastur 
a=input("1 dan 30 gacha son kiriting  ")
if a.isdigit() :
    a = int(a)
    if a>0 and a<30 :
        b = a%10
        c=''
        if a>9 and a<20 :
            c = 'o\'n '
        elif a>19 and a<30 :
            c = 'yigirma '
        if b == 0 :
            c += ''    
        elif b == 1 :
            c += 'bir'
        elif b == 2 :
            c += 'ikki'
        elif b == 3 :
            c += 'uch'
        elif b == 4 :
            c += 'to\'rt'
        elif b == 5 :
            c += 'besh'
        elif b == 6 :
            c += 'olti'
        elif b == 7 :
            c += 'yetti'
        elif b == 8 :
            c += 'sakkiz'
        elif b == 9 :
            c += 'to\'qqiz'
        print(c)
    else :
        print("1 dan 30 gacha son kiritish lozim")
else :
    print("Son kiritish lozim")
