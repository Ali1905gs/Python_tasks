a = int(input("Enter a number (N>0): "))
def f(x):
    k = x
    while x!=1:
        print(f"{x} ")
        if x%2==0:
            x//=2
        else:
            x=3*x+1
        if k<x:
            k = x
    print(1)
    print(f"Max number: {k}")
f(a)
