s = list(map(int,input().split())) #first and end point of house
a = list(map(int,input().split())) # pos of app tree
_ = list(map(int,input().split()))
m = list(map(int,input().split()))#apples
n = list(map(int,input().split()))
x = []
y = []
t = 0
v = 0
for i in range(len(m)):
    x.append(a[0]+m[i])
for j in range(len(n)):
    y.append(a[1]+n[j])
s = list(range(s[0],s[1]))
for i in range(len(x)):
    if x[i] in s:
        t = t +1
for i in range(len(y)):
    if y[i] in s:
        v = v+1
print(t)
print(v)
    
    
    
    
