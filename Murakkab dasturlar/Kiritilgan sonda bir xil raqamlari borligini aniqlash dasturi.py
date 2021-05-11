# Kiritilgan sonda o'xshash raqamlari borligini aniqlash dasturi
xona = int(input("Nechi xonali son kiritmoqchisiz"))
son = int(input('O\'sha sonni kiriting '))
m = 0 ; n=[]
for i in range(0,xona):
    while m<=son:
        n.append(i)
        m//=10
        if n[i] == n[i] :
            print('Kiritilgan sonda bir xil raqamlar mavjud')
        else :
            print("Kiritilgan sonda bir xil raqamlar mavjud emas")