import sys

def dss(depth,M,N):
    if depth >= M:
        print(*arr)
        return
    for i in range(1, N+1):
        arr[depth] = i
        dss(depth+1,M,N)

if __name__ == '__main__' :
    N, M = map(int, sys.stdin.readline().split(' '))
    ds = [i for i in range(1, N+1)]
    arr = [1 for _ in range(M)]
    depth = 0

    dss(depth,M,N)
    
