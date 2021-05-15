def diagonalDifference():
    a = int(input())
    pos = 0
    rev = a-1
    sum = 0
    dum = 0
    for i in range(a):
        arr = list(map(int,input().split()))
        sum = sum +arr[pos]
        pos = pos + 1
        dum = dum +arr[rev]
        rev = rev - 1
    print(abs(sum-dum))
diagonalDifference()


    
