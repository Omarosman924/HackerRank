x = 0
y = 1
z = int(input())
a = int(input())
arr = []
for i in range(int(z/2)+1):
    arr.append([x,y])
    x = x+2
    y = y+2

if a%2==0 :
  x = arr.index([a,a+1])
  arr.reverse()
  y = arr.index([a,a+1])
elif a%2!=0:
       x = arr.index([a-1,a])
       arr.reverse()
       y = arr.index([a-1,a])
print(min([x,y]))
       

