#ml da berilgan masofani m,sm,ml ga aylantiruvchi dastur
a=int(input("Masofani kiriting(iltimos millimetrda kiriting) - "))
b=a//1000
a=a%1000
c=a//10
a=a%10
print(b,"m",c,'sm',a,'ml',sep=' ',end=' .')
