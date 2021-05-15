def compareTriplets():
    x = list(map(int,input().split())) 
    y = list(map(int,input().split()))
    a = 0
    b = 0
    for i in range(3):
        if x[i]>y[i]:
            a = a +1
        elif x[i]<y[i]:
            b = b + 1
    print(a,b)
compareTriplets()
    

