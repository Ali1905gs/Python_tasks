a = int(input("Enter a number : "))
def length(x):
    k=0
    while x>0:
        k+=1
        x//=10
    return k
l = length(a)
p = 1
num1 = 0
num2 = 0
while a>0:
    reqem=a%10
    num1 = reqem*l+num1
    num2 = reqem*p+num2
    a//=10
    l-=1
    p+=1
if num1 == num2 :
    print("True")
else :
    print("False")
