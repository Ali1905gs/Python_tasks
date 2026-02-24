num=int(input("2-lik eded daxil edin:"))
summ=0
quvvet=0
while num>0:
    a1=num%10
    summ=summ+a1*(2**quvvet)
    num//=10
    quvvet+=1
print(summ)
