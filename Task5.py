num=int(input("Natural eded daxil edin:"))
num1=num
num_after=0
while num>0:
    a1=num%10
    num_after=num_after*10+a1
    num//=10
if num1==num_after:
    print("Polindrom")
else :
    print("Deyil")
