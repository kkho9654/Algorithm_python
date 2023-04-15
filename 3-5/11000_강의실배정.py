import sys

if __name__ == '__main__':
    N = int(sys.stdin.readline())
    arr = []
    MAX = 1
    for i in range(N):
        arr.append(list(map(int, sys.stdin.readline().split(' '))))
        if arr[i][1]>MAX:
            MAX = arr[i][1]
    d = [0 for _ in range(MAX+1)]
    for a in arr:
        for i in range(a[0],a[1]):
            d[i] += 1
    # print(d)
    
    print(max(d))