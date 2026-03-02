a=int(input("Eded daxil edin :"))
def sde(x):
    k=0
    for i in range (2,x):
        if x%i==0:
            k+=1
    if k==0:
        return 1
    else :
        return 2
while a>0:
    if sde(a)==2 or a==1:
        print("Eded hipersade deyil")
        break
    a//=10
else:
    print("Eded hipersadedir")
