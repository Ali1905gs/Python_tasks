num=int(input("Natural eded daxil edin:"))
k=0
while num>10:
    a1=num%10
    a2=(num%100)//10
    num//=10
    if a1==a2:
        k+=1
        print("Yes")
        break
if k==0:
    print("No")
