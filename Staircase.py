def staircase():
    b = int(input())
    a = b-1
    for i in range(b):
        s = i+1
        print(' '*a+'#'*s)
        a = a-1
staircase()
