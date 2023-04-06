import sys

if __name__ == '__main__':
    N = int(sys.stdin.readline())
    arr = list(map(int,sys.stdin.readline().split(' ')))
    D = [1000000 for _ in range(N + 100)]
    D[0] = 0
    for idx in range(N):
        for i in range(1, arr[idx]+1):
            if D[idx+i] > D[idx] + 1:
                D[idx+i] = D[idx] + 1
    if D[N-1] == 1000000:
        print(-1)
    else:
        print(D[N-1])
