# Kirtilgan natural sonning nechta raqamdan tashkil topganligini aniqlovchi dastur
n = input("Natural son kirting ")
if n.isdigit():
    n=int(n)
    s=0
    while n>=1 :
        n = n / 10
        s+=1
    print(f"Kiritilgan sonning raqamlari soni {s}")
else :
    print("Natural son kirtih lozim")
