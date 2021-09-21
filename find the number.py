import sys
n = int(sys.stdin.readline())
pac = list(map(int, sys.stdin.readline().split( )))

k = int(sys.stdin.readline())
com = list(map(int, sys.stdin.readline().split( )))

pac.sort()
for i in com :
    lo=0
    hi=n-1
    while lo < hi:
        mid = (lo + hi) // 2
        if pac[mid] < i:
            lo = mid + 1
        elif pac[mid] == i:
            lo = mid
            break
        else:
            hi = mid
    
    if pac[lo] == i :
            print(1)
    else:
        print(0)

