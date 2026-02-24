num=int(input("Natural eded daxil edin:"))
i=2
while num>1:
    if num%i!=0:
        i+=1
    else :
        num=num//i
        print(i)
