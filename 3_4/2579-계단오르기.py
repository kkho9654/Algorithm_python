import sys

def stair(n, arr):
    cum = [0 for _ in range(n+1)]
    cum[0] = arr[0]
    cum[1] = arr[1]
    cum[2] = arr[2] + arr[1]
    for i in range(3, n+1):
        if cum[i-1] != arr[i-1] + cum[i-2]:
            cum[i] = max(cum[i-1] + arr[i], cum[i-2] + arr[i])
        else:
            cum[i] = cum[i-2] + arr[i]
    print(cum)
    
if __name__ == '__main__':
    n = int(input())
    arr = []
    for i in range(n):
        arr.append(int(sys.stdin.readline()))
    arr.insert(0,0)
    stair(n, arr)