#O'ylangan sonni hohlagancha imkoniyatda topuvchi dastur
son=23
yugur=True
while yugur :
    taxmin=int(input("Butun son kiriting:"))
    if taxmin==son :
        print("Tabriklaymiz siz topdingiz ")
        yugur=False
    elif taxmin < son:
        print("Yoq,o'ylangan son kiritilgan sondan kattaroq ")
    else:
        print("Yoq o'ylangan son kiritilgan sondan kichikroq ")
else :
    print("while sikli tugadi .")
    print("tamom")
