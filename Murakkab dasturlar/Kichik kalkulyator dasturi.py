# Kichik kalkulyator dasturi
while True :
    amal = input("Amalni kiriting ( qo'shish/ayirish/ko'paytirish/bo'lish) ")
    son1 = int(input("(Natural son kiritish lozim)Birinchi sonni kiriting  "))
    son2 = int(input("(Natural son kiritish lozim)Ikkinchi sonni kiriting  "))
    if amal=='qoshish' or amal=="qo'shish" or amal=="qo`shish" :
        natija = son1+son2
        print("natija = ",natija)
    elif amal == 'ayirish' :
        natija = son1-son2
        print("natija = ",natija)
    elif amal=="ko'paytirish" or amal=='ko`paytirish' or amal=='kopaytirish':
        natija = son1*son2
        print("natija = ",natija)
    elif amal=="bo'lish" or amal=="bo`lish" or amal=='bolish':
        natija = son1/son2
        print("natija = ",natija)
    else :
        print("Amalni kiritishda xatolik bor\nBosh harflarga va bo'sh joylarda xatolik bo'lishi mumkin")
    
