import sys,heapq
input = sys.stdin.readline

V, E = list(map(int,input().split()))

# union-find array
arr = [i for i in range(V+1)]

def findroot(x):
    while True:
        if arr[x] == x:
            return x
        x = arr[x]
pq = []

for i in range(E):
    a,b,c = list(map(int, input().split()))
    heapq.heappush(pq,(c,a,b))

ans = 0
while pq:
    c,a,b = heapq.heappop(pq)
    aroot = findroot(a)
    broot = findroot(b)
    if aroot!=broot:
        arr[max(aroot,broot)] = min(aroot,broot)
        ans += c

print(ans)