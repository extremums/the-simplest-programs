# Natural sonning barcha bo'luvchilarini topish dasturi
n=input("Natural son kiriting  ")
if n.isdigit():
    n = int(n)
    for i in range(1,n+1):
        if n%i == 0 :
            print(i)
else:
    print("Natural son kirtish lozim  ")
