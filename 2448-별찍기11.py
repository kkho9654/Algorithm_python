import sys, math
# 총 가로길이는 5 * 2^n + 2^n-1
# (5*2^k-1) / 2


print = sys.stdout.write
N = int(sys.stdin.readline())
k = int(math.log2(N/3))
arr = [[' ' for _ in range(5*(2**k) + (2**k) - 1)] for _ in range(N)]

def star(k, y ,x):
    # print(f'x = {x} , y= {y}')
    if k == 0:
        arr[y][x] = '*'
        arr[y+1][x+1] = '*'
        arr[y+1][x-1] = '*'
        arr[y+2][x] = '*'
        arr[y+2][x+1] = '*'
        arr[y+2][x+2] = '*'
        arr[y+2][x-1] = '*'
        arr[y+2][x-2] = '*'
        return
    star(k-1 ,y , x)
    if k == 1:
        tmp = 3
    else:
        tmp = round(5*2**(k-2)) + 2**(k-2)
    star(k-1, y + 3*(2**(k-1)),x - tmp)
    star(k-1, y + 3*(2**(k-1)),x + tmp)

star(k,0,round(5*2**(k-1) + 2**(k-1)-1))
for a in arr:
    for t in a:
        print(t)
    print('\n')
