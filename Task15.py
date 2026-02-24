n=int(input())
k=1
while k<=n:
    y=0
    t=0
    s=k
    while s>0:
        a1=s%10
        if a1!=0 and k%a1==0:
            y+=1
        t+=1
        s//=10
    if y==t:
        print(k)
    k+=1
