import sys, heapq, collections
input = sys.stdin.readline

N,M = list(map(int,input().split()))

pq = []
road = collections.defaultdict(list)
for i in range(M):
    a,b,c = list(map(int,input().split()))
    heapq.heappush(pq,(c,a,b))
    heapq.heappush(road[a], (c,b))
    heapq.heappush(road[b], (c,a))
c,a,b = heapq.heappop(pq)

if N == 2:
    print(0)
    exit()
visited = set()
visited.add(a)
visited.add(b)
candidatehome = []
for i in road[a]:
    _, ed = i
    if ed not in visited:
        heapq.heappush(candidatehome,i)
for i in road[b]:
    _, ed = i
    if ed not in visited:
        heapq.heappush(candidatehome,i)
total = c
v = 1
mx = 0
while candidatehome:
    if v==N-1:
        break
    cost , edge = heapq.heappop(candidatehome)
    if edge in visited:
        continue
    visited.add(edge)
    for i in road[edge]:
        _, ed = i
        if ed not in visited:
            heapq.heappush(candidatehome,i)
    total+=cost
    if mx < cost:
        mx = cost
    v+=1

print(total-mx)