n=int(input("10 luq eded daxil edin : "))
quvvet=0
sum=0
while n>0:
    k=n%2
    n=n//2
    sum=sum+k*10**quvvet
    quvvet+=1
print(sum)
