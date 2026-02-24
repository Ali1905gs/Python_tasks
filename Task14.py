n=int(input())
k=1
while k < n:
    count=0
    l=k
    while l>0:
        count+=1
        l=l//10
    s=k**2
    p=s%10**count
    if p==k:
        print(k,"*",k,"=",s)
    else :
        pass
    k+=1
