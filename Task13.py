print("1.) Rakamlari topla","2.) Rakamlari carp","3.) Cikmak icin her hangi tusa bas",sep="\n")
n=int(input("2 reqemli eded daxil edin: "))
a=int(input("Bir secim edin: "))
if a==1:
    s=0
    while n>0:
        s=s+n%10
        n=n//10
    print(s)
elif a==2:
    p=1
    while n>0:
        p=p*(n%10)
        n=n//10
    print(p)
else:
    exit()
