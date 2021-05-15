def BTR():
    y = 1000000000000
    x = 0
    mx = []
    a = int(input())
    mn = []
    arr = list(map(int,input().split()))
    for i in range(a):
        if arr[i]>=x:
            x = arr[i]
            mx.append(arr[i])
        if arr[i]<=y:
            y = arr[i]
            mn.append(arr[i])
            
    print(len(list(dict.fromkeys(mx)))-1,len(list(dict.fromkeys(mn)))-1)

    
BTR()
        
        
