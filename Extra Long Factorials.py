for i in range(int(input())):
    res =  "".join(reversed(''.join(sorted(str(input())))))
    if res[1:] == res[:-1]:
        print('no answer')
    else:
        print(res)
