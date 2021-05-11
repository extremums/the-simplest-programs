# 1 dan 7 gacha son kiritilsin o'sha sonni haftani nechinchi kuni ekanligini aniqlang
'''while True:
    a=input("Natural son kiriting  ")
    if a.isdigit():
        a=int(a)
        if a>0 and a<8:
            if a==1:
                print("Dushanba")
            elif a==2:
                print("Seshanba")
            elif a==3 :
                print("Chorshanba")
            elif a==4 :
                print("Payshanba")
            elif a==5:
                print("Juma")
            elif a==6:
                print("Shanba")
            elif a==7 :
                print("Yakshanba")
        else:
            print("0 dan katta 8 dan kichik son kiritish lozim")
    else:
        print("Natural son kiritish kerak")'''
'''while True:
    a=input("Yilni kiriting (natural son bo'lishi lozim)  ")
    if a.isdigit():
        a=int(a)
        if a%100 !=0 and a%400!=0 and a%4==0:
            print("Kiritilgan yil kabisa yili ")
        else:
            print("Kiritilgan yil kabisa yili emas")
    else:
        print("Natural son kiritish lozim ")'''
# Kiritilgan sonni qaysi oy ekanligini chiqarish dasturi
'''while True:
    a=input("Natural son kiriting  ")
    if a.isdigit:
        a=int(a)
        if a>=0 and a<=12:
            if a==1:
                print("Kiritilgan son bu Yanvar oyi")
            elif a==2:
                print("Kiritilgan son bu Fevral oyi")
            elif a==3 :
                print("Kiritilgan son bu Mart oyi")
            elif a==4 :
                print("Kiritilgan son bu Aprel oyi")
            elif a==5:
                print("Kiritilgan son bu May oyi")
            elif a==6:
                print("Kiritilgan son bu Iyun oyi")
            elif a==7:
                print("Kiritilgan son bu Iyul oyi")
            elif a==8 :
                print("Kiritilgan son bu Avgust oyi")
            elif a==9:
                print("Kiritilgan son bu Sentabr oyi")
            elif a==10:
                print("Kiritilgan son bu Oktabr oyi")
            elif a==11 :
                print("Kiritilgan son bu Noyabr oyi")
            elif a==12 :
                print("Kiritilgan son bu Dekabr oyi")
        else:
            print("Kiritilgan son 0 dan katta 13 dan kichik bo'lish lozim")
    else:
        print("Natural son kiritish lozim  ")'''
# Kiritilgan sonni matn korinishiga o'tqazuvchi dastur
'''while True:
    a=input("Natural son kiriting  ")
    if a.isdigit():
        a=int(a)
        soz = '' 
        if a>9 and a<20 :
            soz += " o'n "
        elif a>19 and a<30:
            soz += " yigirma "
        elif a>29 and a<40:
            soz += " o'ttiz "
        elif a>39 and a<50:
            soz += " qirq "
        elif a>49 and a<50:
            soz += " ellik "
        elif a>59 and a<70:
            soz += " oltmish "
        elif a>69 and a<80:
            soz += " yetmish "
        elif a>79 and a<90:
            soz+=" sakson "
        elif a>89 and a<100:
            soz += "to'qson"
        if a%10==1:
            soz+=" bir "
        elif a%10==2:
            soz+=" ikki "
        elif a%10==3:
            soz+=" uch "
        elif a%10==4:
            soz+=" to'rt "
        elif a%10==5:
            soz+=' besh '
        elif a%10==6:
            soz+=' olti '
        elif a%10==7:
            soz += " yetti "
        elif a%10==8:
            soz += " sakkiz "
        elif a%10==9:
            soz += " to'qqiz "
        print(soz)
    else:
        print("Natural son kiritish kerak ")'''
# Kiritilgan sonni matn korinishiga o'tqazuvchi dastur
'''while True:
    a=input("Natural son kiriting  ")
    if a.isdigit():
        a=int(a)
        soz = '' 
        if (a%1000)==1:
            soz+=" bir "
        elif a%10==2:
            soz+=" ikki "
        elif a%10==3:
            soz+=" uch "
        elif a%10==4:
            soz+=" to'rt "
        elif a%10==5:
            soz+=' besh '
        elif a%10==6:
            soz+=' olti '
        elif a%10==7:
            soz += " yetti "
        elif a%10==8:
            soz += " sakkiz "
        elif a%10==9:
            soz += " to'qqiz "
        if (a%100)//10==1 :
            soz += " o'n "
        elif (a%100)//10==2:
            soz += " yigirma "
        elif (a%100)//10==3:
            soz += " o'ttiz "
        elif (a%100)//10==4:
            soz += " qirq "
        elif (a%100)//10==5:
            soz += " ellik "
        elif (a%100)//10==6:
            soz += " oltmish "
        elif (a%100)//10==7:
            soz += " yetmish "
        elif (a%100)//10==8:
            soz+=" sakson "
        elif (a%100)//10==9:
            soz += "to'qson"
        if a%10==1:
            soz+=" bir "
        elif a%10==2:
            soz+=" ikki "
        elif a%10==3:
            soz+=" uch "
        elif a%10==4:
            soz+=" to'rt "
        elif a%10==5:
            soz+=' besh '
        elif a%10==6:
            soz+=' olti '
        elif a%10==7:
            soz += " yetti "
        elif a%10==8:
            soz += " sakkiz "
        elif a%10==9:
            soz += " to'qqiz "
        print(soz)
    else:
        print("Natural son kiritish kerak ")'''









