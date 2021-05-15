x = list(map(int,input().split()))
mx = 0
mn = x[0]
for i in range(len(x)):
    if x[i]>mx:
        mx = x[i]
    if x[i]<mn:
        mn = x[i]

for j in range(mn,mx+1):
    for i in range(len(x)):
        if j == x[i]:
            print(j)
    
