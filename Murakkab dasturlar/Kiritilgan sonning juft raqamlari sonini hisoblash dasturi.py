# Kiritilgan sonning juft raqamlari sonini hisoblash dasturi
i = int(input("Natural son kiriting  "))
s =0
n =0
while i >= 1:
    i=i%10
    s+=i%10
    print(s)
