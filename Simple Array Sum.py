def simpleArraySum():
    y = int(input())
    sum = 0
    x = list(map(int, input().split()))
    for i in range(y):
        sum =x[i] + sum
    print(sum)
