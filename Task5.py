a = int(input("Enter N: "))
b = int(input("Enter P: "))
def length(x):
    k=-1
    while x>0:
        k+=1
        x//=10
    return k
b = b+length(a)
p = a
s = 0
while p>0:
    s=s+(p%10)**b
    b-=1
    p//=10
if s%a == 0:
    print(f"K: {s//a}")
else:
    print("K: None")
