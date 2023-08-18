import sys
input = sys.stdin.readline

n,m = list(map(int,input().split()))

arr = [i for i in range(n+1)]

for _ in range(m):
    cal, a, b = list(map(int,input().split()))
    if cal == 0:
        aroot = arr[a]
        broot = arr[b]
        while aroot != arr[aroot]:
            aroot = arr[aroot]
        while broot != arr[broot]:
            broot = arr[broot]

        if aroot > broot:
            arr[broot] = aroot
        else:
            arr[aroot] =broot

    elif cal == 1:
        aroot = arr[a]
        broot = arr[b]
        while aroot != arr[aroot]:
            aroot = arr[aroot]
        while broot != arr[broot]:
            broot = arr[broot]
        if aroot == broot:
            print('YES')
        else:
            print('NO')