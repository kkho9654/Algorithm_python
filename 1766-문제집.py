import sys, heapq
input = sys.stdin.readline

N, M = list(map(int,input().strip().split()))
nums = [0 for i in range(N)]
graph = [[] for i in range(N)]
queue = []
for _ in range(M):
    A,B = list(map(int,input().strip().split()))
    graph[A-1].append(B-1)
    nums[B-1] += 1
ans = []
for i in range(N):
    if nums[i] == 0:
        heapq.heappush(queue, i)

while queue:
    hp = heapq.heappop(queue)
    ans.append(hp+1)

    for h in graph[hp]:
        nums[h] -= 1
        if nums[h] == 0:
            heapq.heappush(queue, h)

print(*ans)
