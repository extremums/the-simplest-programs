#Berilgan sonlarning raqamlari yig'indisi
a=int(input("Son kiriting - "))
a1=a%10
a2=a%100//10
a3=a%1000//100
a4=a//1000
print("Berilgan sonning raqamlari yig'indisi",a1+a2+a3+a4,sep='=')
