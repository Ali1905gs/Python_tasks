num=100
while num<=999:
    a1=num//100
    a2=(num//10)%10
    a3=num%10
    num_after=a1**3+a2**3+a3**3
    if num == num_after:
        print(num)
    else :
        pass
    num+=1
