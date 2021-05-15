c = str(input())
s = c[3:]
if c[0]+c[1]=='12'and c[-2:]=='AM':
    s = '00:'+s
    s = s.replace(c[-2:],'')
    print(s)
elif (c[0]+c[1]=='12'and c[-2:]=='PM') or c[-2:]=='AM':
    c = c.replace(c[-2:],'')
    print(c)
elif c[-2:]=='PM':
    s = str(int(c[0]+c[1])+12)+':'+s
    s = s.replace(c[-2:],'')
    print(s)
else:
    print(c)
