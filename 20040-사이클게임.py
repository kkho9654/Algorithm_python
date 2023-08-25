import sys
input = sys.stdin.readline

n,m = map(int,input().split())
parent = [i for i in range(n)]
rank = [0]*n
ans = 0

def find(a):
    if parent[a]!=a:
        parent[a] = find(parent[a])
    return parent[a]

def union(a,b):
    p1 = find(a)
    p2 = find(b)

    if p1 == p2:
        return True
    
    if rank[p1] > rank[p2]:
        parent[p2] = p1
    elif rank[p2] > rank[p1]:
        parent[p1] = p2
    else:
        parent[p2] = p1
        rank[p1] += 1

flag = True
for i in range(m):
    a,b = map(int,input().split())
    if flag:
        if union(a,b):
            flag = False
            ans = i+1

print(ans)