while True:
    a=input("3 xonali son kiriting(bo'lmasa dastur xato ishlashi mumkin) ")
    if a.isdigit():
        a=int(a)
        a1=a//100 ; a2=(a%100)//10 ; a3=a%10
        if a1==a2 or a1==a3 or a2==a3:
            print("O'xshash raqamlari mavjud")
        else:
            print("O'xshash raqamlari mavjudmas")
    else:
        print('Natural son kiritish lozim')
