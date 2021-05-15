
from decimal import *
def plusMinus():
    pos = 0
    neg = 0
    zero = 0
    a = int(input())
    arr = list(map(int,input().split()))
    for i in range (a):
        if arr[i]<0:
            neg = neg + 1
        elif arr[i]>0:
            pos = pos +1
        else:
            zero = zero+1
    getcontext().prec = 6
    print(pos/a)
    print(neg/a)
    print(zero/a)
plusMinus()

    
