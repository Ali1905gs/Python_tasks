a1=1
a2=1
print(a1)
print(a2)
while a2<=50:
    q=a1+a2
    if q>50:
        break
    a1=a2
    a2=q
    print(a2)
