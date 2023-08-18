import sys

N = int(sys.stdin.readline())
arr = []

def bt(depth, num, arr):
    arr.append(num)
    if depth == 0:
        mx = 10
    else:
        mx = (num%10)
    num *= 10
    for i in range(mx):
        num += i
        bt(depth+1, num,arr)
        num -= i

bt(0,0,arr)

try:
    print(sorted(arr)[N])
except:
    print(-1)
