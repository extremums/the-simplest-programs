# # Grafik interfeys bilan ishlash mavzusi
# from tkinter import *

# oyna = Tk()

# oyna.title('✯✵❃ Mening dasturim ✯✵❃')

# oyna.geometry('310x110')

# oyna.configure(background='yellow')

# mening_nishonim = Label(oyna,width=40,height=5,bg='yellow',text='')

# mening_nishonim.grid(row=0,column=0)

# def text():
#     mening_nishonim.config(text="Hello !\nWhat's your name ?\nMy name is Nurullo asistent")

# mening_tugmam = Button(oyna,text=' Meni bos',width=10,command=text)

# mening_tugmam.grid(row=1,column=0)

# oyna.mainloop()

# # Rangi yashil , o'lchami 100x100 bo'lgan "Mening birinchi ilovam" nomli 
# # GUI oynasini yarating .Unda 'Salom O'zbekiston' xabarini chiqaruvchi dastur
# from tkinter import*

# oyna = Tk()
# oyna.title("Mening birinchi ilovam")
# oyna.geometry('100x100')
# oyna.configure(background='green')

# nishon = Label(oyna,width=20,height=2,bg='green',text="")
# nishon.grid(row=0,column=0)

# def text():
#     nishon.config(text="Salom O'zbekiston !!!")
#     def text():
#         nishon.config(text="Salom O'zbekiston !!!")

# tugma=Button(oyna,width=7,text="Meni boss",command=text)
# tugma.grid(row=3,column=0) 

# oyna.mainloop()

# # raangi=pushti ; o'lchami=250x150 ; nomi="Mevalar" ; 4 ta mevadan birini tanlash
# # imkonini beruvchi dastur yarating.
# from tkinter import*

# ilova = Tk()
# ilova.title(" Sevimli mevalar ")
# ilova.geometry('250x150')
# ilova.configure(background='pink')

# matn = Label(ilova,width=25,height=3,background='pink',text='')
# matn.grid(row=1,column=0)

# def text():
#     matn.config(text="Siz olma mevasini yaxshi ko'rasiz\nE'tiboringiz uchun raxmat!!!")
# tugma = Button(ilova,width=10,text='Olma',command=text)
# tugma.grid(row=0,column=1)

# def text():
#     matn.config(text="Siz banan mevasini yaxshi ko'rasiz\nE'tiboringiz uchun raxmat!!!")
# tugma1 = Button(ilova,width=10,text='Banan',command=text)
# tugma1.grid(row=1,column=1)

# def text():
#     matn.config(text="Siz kivi mevasini yaxshi ko'rasiz\nE'tiboringiz uchun raxmat!!!")
# tugma2 = Button(ilova,width=10,text='Kivi',command=text)
# tugma2.grid(row=2,column=1)

# def text():
#     matn.config(text="Siz tut mevasini yaxshi ko'rasiz\nE'tiboringiz uchun raxmat!!!")
# tugma3 = Button(ilova,width=10,text='Tut',command=text)
# tugma3.grid(row=60,column=1)

# ilova.mainloop()

# # Boshqacha yoli
# from tkinter import*
# ilova=Tk()
# ilova.config(bg='pink')
# ilova.geometry('250x150')
# ilova.title('Mevalar')

# mevalar=('Olma','Behi','Gilos','Banan')

# tanlash = IntVar()
# tanlash.set('Sevimli mevangizni tanlang')

# natija = OptionMenu(ilova,tanlash,*mevalar)
# natija.grid(row=0,column=0)

# ilova.mainloop()

# # Yana bir yo'ii
# from tkinter import*
# ilova = Tk()
# ilova.title('Mevalar')
# ilova.geometry('250x150')
# ilova.config(bg='pink')

# mevalar = StringVar()

# olma=Radiobutton(ilova,width=12,height=4,bg='red',text='Olma',variable=mevalar,value='olma')
# olma.grid(row=0,column=0,sticky=W)
# olma.select()

# behi = Radiobutton(ilova,width=12,height=4,bg='red',text='Behi',variable=mevalar,value='behi')
# behi.grid(row=0,column=1,sticky=W)
# behi.select()

# gilos = Radiobutton(ilova,width=12,height=4,bg='red',text='Gilos',variable = mevalar,value='gilos')
# gilos.grid(row=1,column=0,sticky=W)
# gilos.select()

# banan = Radiobutton(ilova,width=12,height=4,bg='red',text='Banan',variable=mevalar,value='banan')
# banan.grid(row=1,column=1,sticky=W)
# banan.select()

# ilova.mainloop()

# # GUI dan foydalanob 1 dan n gacha tasodifiy 10 ta sonni chiqaruvchi dastur
# from tkinter import*
# from random import*
# def tasodifiy():
#     son = int(son_ol.get())
#     natija.delete(0.0,END)
#     for i in range(10):
#         tasodif = str(randint(1, son))+'\n'
#         natija.insert(END,tasodif)
# ilova = Tk()
# ilova.title('Tasodifiy son')
# ilova.config(bg='yellow')
# ilova.geometry('250x250')

# son_matni = Label(ilova,text='Sonni kirit : ',bg='yellow')
# son_matni.grid(row=0,column=0)

# natija_matni = Label(ilova,bg='yellow',text='\nSongacha tasodifiy sonlar')
# natija_matni.grid(row=2,column=0)

# son_ol = Entry(ilova,bg='white',width=10)
# son_ol.grid(row=1,column=0)

# tugma = Button(ilova,text='Tasodifiy sonlar',command=tasodifiy)
# tugma.grid(row=1,column=1)

# natija = Text(ilova,width=6,height=10)
# natija.grid(row=3,column=0)

# ilova.mainloop()

# # n ga karrali 10 ta sonni chiqarish dasturi (GUI dan foydalanib)
# from tkinter import*
# def karrali():
#     son = son_kirit.get()
#     natija.delete(0.0,END)
#     if son.isdigit():
#         son=int(son)
#         for i in range(1,11):
#             natija_chiq = str(son*i)+'\n'
#             natija.insert(END,natija_chiq)
#     else:
#         natija.insert(END,'Iltimos natural son kiriting')
# ilova = Tk()
# ilova.title('Karrali son')
# ilova.geometry('250x250')
# ilova.config(bg='blue')

# son_matni = Label(ilova,bg='blue',text='Natural son kiriting ')
# son_matni.grid(row=0,column=0)

# natija_matni = Label(ilova,bg='blue',text='Songa karrali sonlar')
# natija_matni.grid(row=2,column=0)

# son_kirit = Entry(ilova,width=8,bg='yellow')
# son_kirit.grid(row=1,column=0)

# natija = Text(ilova,width=20,height=10,bg='yellow')
# natija.grid(row=3,column=0)
# tugma = Button(ilova,text='Karrali',bg='red',command=karrali)
# tugma.grid(row=1,column=1)

# ilova.mainloop()

# # Kiritilgan songa kiritilgan ikkinchi soncha karrali sonlarni chiqarish dasturi
# from tkinter import*
# def karrali():
#     son = int(son_ol.get())
#     karrali = int(karrali_ol.get())
#     natija.delete(0.0,END)
#     for i in range(1,karrali+1):
#         natija1 = str(i*son)+'\n'
#         natija.insert(END,natija1)
# ilova = Tk()
# ilova.title('Karrali son')
# ilova.geometry('250x250')
# ilova.config(bg='blue')

# son1 = Label(ilova,bg='blue',text='Son kiriting ')
# son1.grid(row=0,column=0)

# karrali1 = Label(ilova,bg='blue',text='Nechta karrali son')
# karrali1.grid(row=0,column=1)

# son_ol = Entry(ilova,width=6,bg='red')
# son_ol.grid(row=1,column=0)

# karrali_ol = Entry(ilova,bg='red',width=6)
# karrali_ol.grid(row=1,column=1)

# natija = Text(ilova,width=10,bg='red')
# natija.grid(row=3,column=0)

# tugma = Button(ilova,width=20,bg='yellow',text='Karrali son',command=karrali)
# tugma.grid(row=2,column=0)

# ilova.mainloop()
# 
# # n ta tub sonni chiqarish dasturi
# from tkinter import*
# from math import*
# def tub():
#     n = int(son.get())
#     natija.delete(0.0,END)
#     b=2
#     s=0
#     while True:
#         for i in range(2,int(sqrt(b)+1)):
#             if b%i==0:
#                 break
#         else:
#             s+=1
#             satr = str(b)+'\n'
#             natija.insert(END,satr)
#         b+=1
#         if s==n:
#             break
# ilova = Tk()
# ilova.title('Tub son')
# ilova.geometry('250x250')
# ilova.config(bg='red')

# nechta = Label(ilova,bg='red',text='Nechta tub son chiqsin')
# nechta.grid(row=0,column=0)

# son = Entry(ilova,bg='green',width=5)
# son.grid(row=1,column=0)

# natija = Text(ilova,bg='green',width=6,height=10)
# natija.grid(row=2,column=0)

# tugma = Button(ilova,bg='green',text='Tub sonlar',command = tub)
# tugma.grid(row=1,column=1)

# ilova.mainloop()

# # Kiritilgan ikki sonni EKUB ini hisoblash dasturi
# from tkinter import*
# from math import*

# def ekub():
#     a=int(son.get())
#     b=int(son1.get())
#     natija.delete(0.0,END)
#     while a!=0 and b!=0:
#         if a>b:
#             a%=b
#         else:
#             b%=a
#     ekub_2=a+b
#     natija.insert(END,ekub_2)
# ilova = Tk()
# ilova.title('EKUB(a,b)')
# ilova.config(bg='yellow')
# ilova.geometry('250x250')

# son_matni = Label(ilova,bg='yellow',text='Birinchi son : ')
# son_matni.grid(row=0,column=0)

# son1_matni = Label(ilova,bg='yellow',text='Ikkinchi son : ')
# son1_matni.grid(row=0,column=1)

# son = Entry(ilova,bg='pink',width=6)
# son.grid(row=1,column=0)

# son1 = Entry(ilova,bg='pink',width=6)
# son1.grid(row=1,column=1)

# natija_matni = Label(ilova,bg='yellow',text='Natija')
# natija_matni.grid(row=2,column=0)

# natija = Text(ilova,bg='pink',width=6,height=10)
# natija.grid(row=3,column=0)

# tugma = Button(ilova,bg='pink',text='EKUB(a;b)',command=ekub)
# tugma.grid(row=1,column=3)

# ilova.mainloop()

# from tkinter import*
# from random import*

# def tekshir():
#     natija.delete(0.0,END)
#     bir.delete(0.0,END)
#     ikki.delete(0.0,END)
#     n = int(son.get())
#     a=randint(50,200)
#     b=randint(100,200)
#     bir.insert(END,a)
#     ikki.insert(END,b)
#     c=a+b
#     if n==int(c):
#         natija.insert(END,"To'g'ri javob BARAKALLA")
#     elif n!=int(c):
#         natija.insert(END,"Noto'g'ri javob yaxshilab o'ylab ko'r")
# ilova = Tk()
# ilova.title("😊Tog'ri top😊")
# ilova.geometry('250x250')
# ilova.config(bg='yellow')

# bir_son = Label(ilova,text='Birinchi son : ',bg='yellow')
# bir_son.grid(row=0,column=0)

# ikki_son = Label(ilova,text='Ikkinchi son : ',bg='yellow')
# ikki_son.grid(row=0,column=1)

# bir = Text(ilova,bg='pink',width=6,height=1)
# bir.grid(row=1,column=0)

# ikki = Text(ilova,bg='pink',width=6,height=1)
# ikki.grid(row=1,column=1)

# natija = Text(ilova,width=20,height=1,bg='pink')
# natija.grid(row=4,column=0)

# natij_matni = Label(ilova,text="Ikki son yig'indisi :",bg='yellow')
# natij_matni.grid(row=2,column=0)

# son = Entry(ilova,width=6,bg='pink')
# son.grid(row=2,column=1)

# natija_matni=Label(ilova,text="Natija : ",bg='yellow')
# natija_matni.grid(row=3,column=0)

# tugma = Button(ilova,text="Qabul qil",bg='pink',width=12,command=tekshir)
# tugma.grid(row=2,column=2)

# ilova.mainloop()    

# from tkinter import*

# def qosh():
#     a = float(son.get())
#     b = float(son1.get())
#     natija.delete(0.0,END)
#     natija.insert(END,a+b)
# def ayir():
#     a = float(son.get())
#     b = float(son1.get())
#     natija.delete(0.0,END)
#     natija.insert(END,a-b)
# def kop():
#     a = float(son.get())
#     b = float(son1.get())
#     natija.delete(0.0,END)
#     natija.insert(END,a*b)
# def bol():
#     a = float(son.get())
#     b = float(son1.get())
#     natija.delete(0.0,END)
#     natija.insert(END,a/b)

# ilova = Tk()
# ilova.title('Calculate')
# ilova.geometry('250x250')
# ilova.config(bg='yellow')

# bir = Label(ilova,text='Birinchi son : ',bg='yellow')
# bir.grid(row=0,column=0)

# ikki = Label(ilova,text='Ikkinchi son : ',bg='yellow')
# ikki.grid(row=0,column=1)

# natija_matni = Label(ilova,text='Natija : ',width=6,height=1,bg='yellow')
# natija_matni.grid(row=3,column=0)

# son = Entry(ilova,bg='pink',width=10)
# son.grid(row=1,column=0)

# son1 = Entry(ilova,bg='pink',width=10)
# son1.grid(row=1,column=1)

# natija = Text(ilova,width=10,height=1,bg='pink')
# natija.grid(row=3,column=1)

# qosh = Button(ilova,text="Qo'shish",bg='pink',width=6,height=1,command=qosh)
# qosh.grid(row=2,column=0)

# ayir = Button(ilova,text="Ayirish",bg='pink',width=6,height=1,command=ayir)
# ayir.grid(row=2,column=1)

# bol = Button(ilova,text="Bo'lish",bg='pink',width=6,height=1,command=bol)
# bol.grid(row=2,column=2)

# kop = Button(ilova,text="Ko'paytirish",bg='pink',width=8,height=1,command=kop)
# kop.grid(row=2,column=5)

# ilova.mainloop()


from tkinter import*
from decimal import*
window = Tk()
window.title('Calculator')

buttons = (('7','8','9','/'),('4','5','6','*'),
            ('1','2','3','-'),('0','.','=','+'))
satr=''
t = []
def calculate():
    global t
    global label
    natija = 0
    a=Decimal(t.pop())
    amal = t.pop()    
    b=Decimal(t.pop())
    if amal=='+':
        natija = b+a
    if amal == '-':
        natija = b-a
    if amal == '/':
        natija = b/a
    if amal == '*':
        natija = b*a
    label.configure(text=str(natija))
def click(text):
    global satr
    if text=='C':
        t.clear()
        satr=''
        label.configure(text='0')
    elif '0'<=text<='9':
        satr+=text
        label.configure(text=satr)
    elif text=='.':
        if satr.find('.')==-1:
            satr+=text
            label.configure(text=satr)
    else:
        if len(t)>=2:
            t.append(label['text'])
            calculate()
            t.clear()
            t.append(label['text'])
            satr=''
            if text!='=':
                t.append(text)
        else:
            if text!='=':
                t.append(label['text'])
                t.append(text)
                satr=''                
                label.configure(text='0')
label = Label(window,text='0',width=35)
label.grid(row=0,column=0,columnspan=4,sticky='nsew')
button = Button(window,text='C',command=lambda text='C':click(text))
button.grid(row=1,column=3,sticky='nsew')
for row in range(4):
    for col in range(4):
        button = Button(window,text=buttons[row][col],
                        command=lambda row=row,col=col:
                        click(buttons[row][col]))
        button.grid(row=row+2,column=col,sticky='nsew')
window.mainloop()



# n ta tub sonni chiqarish dasturi
from tkinter import*
from math import*
def tub():
    n = int(son.get())
    natija.delete(0.0,END)
    b=2
    s=0
    while True:
        for i in range(2,int(sqrt(b)+1)):
            if b%i==0:
                break
        else:
            s+=1
            satr = str(b)+'\n'
            natija.insert(END,satr)
        b+=1
        if s==n:
            break
ilova = Tk()
ilova.title('Tub son')
ilova.geometry('250x250')
ilova.config(bg='red')

nechta = Label(ilova,bg='red',text='Nechta tub son chiqsin')
nechta.grid(row=0,column=0)

son = Entry(ilova,bg='yellow',width=5)
son.grid(row=1,column=0)

natija = Text(ilova,bg='yellow',width=6,height=10)
natija.grid(row=2,column=0)

tugma = Button(ilova,bg='yellow',text='Tub sonlar',command = tub)
tugma.grid(row=1,column=1)

ilova.mainloop()

# Kiritilgan ikki sonni EKUB ini hisoblash dasturi
from tkinter import*
from math import*

def ekub():
    a=int(son.get())
    b=int(son1.get())
    natija.delete(0.0,END)
    while a!=0 and b!=0:
        if a>b:
            a%=b
        else:
            b%=a
    ekub_2=a+b
    natija.insert(END,ekub_2)
ilova = Tk()
ilova.title('EKUB(a,b)')
ilova.config(bg='yellow')
ilova.geometry('250x250')

son_matni = Label(ilova,bg='yellow',text='Birinchi son : ')
son_matni.grid(row=0,column=0)

son1_matni = Label(ilova,bg='yellow',text='Ikkinchi son : ')
son1_matni.grid(row=0,column=1)

son = Entry(ilova,bg='pink',width=6)
son.grid(row=1,column=0)

son1 = Entry(ilova,bg='pink',width=6)
son1.grid(row=1,column=1)

natija_matni = Label(ilova,bg='yellow',text='Natija')
natija_matni.grid(row=2,column=0)

natija = Text(ilova,bg='pink',width=6,height=10)
natija.grid(row=3,column=0)

tugma = Button(ilova,bg='pink',text='EKUB(a;b)',command=ekub)
tugma.grid(row=1,column=3)

ilova.mainloop()





















