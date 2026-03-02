a = int(input("Enter a number : "))
def length(x):
    k=0
    while x>0:
        k+=1
        x//=10
    return k
if length(a)%2==1:
    print("Invalid")
else:
    t=""
    setr=str(a)
    for i in range (0,len(setr),2):
        t=t+setr[i+1]*int(setr[i])
    print(t)
