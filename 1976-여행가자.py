import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

parent = [i for i in range(N)]

def union(x,y):
    root_x = find(x)
    root_y = find(y)

    if root_x == root_y:
        return
    
    parent[root_y] = parent[root_x]

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

for i in range(N):
    arr = list(map(int,input().split()))
    for j in range(N):
        if arr[j] == 1:
            union(i,j)

plan = list(map(int,input().split()))
for i in range(1,M):
    if find(plan[i] -1) != find(plan[i-1]-1):
        print('NO')
        exit(0)
print('YES')
    