def birthdayCakeCandles():
    a = int(input())
    arr = list(map(sum,input().split()))
    c = 0
    for i in range (a):
        if arr[i]==max(arr):
            c = c+1
    print(c)
birthdayCakeCandles()
