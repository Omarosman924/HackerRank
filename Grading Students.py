def g(x):
    y = x%10
    if x>=37:
        if y>=3 and y<=4:
            return ((int(x/10))*10)+5
        elif y>=8 and y<=9:
            return ((int(x/10)+1)*10)
        else:
            return x
    else :
        return x
arr = []
a = int(input())
for i in range(a):
    arr.append(int(input()))
arr = list(map(g,arr))
for j in range(a):
    print(arr[j])
