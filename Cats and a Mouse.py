a = int(input())
res = []
for i in range(a):
    arr = list(map(int,input().split()))
    if abs(arr[0]-arr[2])<abs(arr[1]-arr[2]):
        res.append("Cat A")
    elif abs(arr[1]-arr[2])<abs(arr[0]-arr[2]):
        res.append("Cat B")
    else:
        res.append("Mouse C")
for j in range(a):
    print(res[j])
