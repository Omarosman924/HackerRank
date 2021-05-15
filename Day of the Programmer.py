y = int(input())
x = 1700
s =[2100,2200,2300,2500,2600]
years = []
for i in range(250):
    years.append(x)
    x = x + 4

if y in years  and y not in s:
    print("12.09."+str(y))
elif y == 1918:

    print("26.09."+str(y))
else:
    print("13.09."+str(y))

