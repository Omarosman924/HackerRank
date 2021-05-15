x = tuple(map(int,input().split()))
s = []
y = list(x)
for i in range(len(x)):
    y.pop(i)
    s.append(sum(y))
    y = list(x)
print(min(s),max(s))
