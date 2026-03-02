a = int(input("Enter a number (N>0): "))
print(f"Decimal : {a} ")
def Bin(x):
    b = 0
    quvvet = 0
    while x>0:
        k=x%2
        b=b+k*10**quvvet
        x//=2
        quvvet+=1
    return b
l = Bin(a)
print(f"Binary: {l} ")
def pol(y):
    num_after = 0
    while y>0:
        num_after=num_after*10+y%10
        y//=10
    return num_after
if pol(l) == l and pol(a) == a:
    print("Polindrome type is Decimal and Binary")
elif pol(l) != l and pol(a) == a:
    print("Plindrome type is only Decimal")
elif pol(l) == l and pol(a) != a:
    print("Plindrome type is only Binary")
else :
    print("Plindrome type is neither Decimal nor Binary")
