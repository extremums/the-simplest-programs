# Karra jadvalini o'quvchidan so'rash
jadval = 8
for i in range (1,11) :
    print(jadval,'x',i,'= ?')
    javob = input()
    if javob == 'bilmayman':
        break
    togri = jadval * i
    if javob == togri:
        print("Barakalla")
    else :
        print("Noto'g'ri javob : ",togri)
        print("Tugadi")
