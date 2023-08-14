import sys,collections
input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)
answer=[0]*(N+1)

for _ in range(N-1):
    x, y = list(map(int, input().strip().split(' ')))
    graph[x].append(y)
    graph[y].append(x)


queue = collections.deque([1])
visited[1] = True
while queue:
    x = queue.popleft()
    arr = graph[x]
    for a in arr:
        if not visited[a]:
            answer[a] = x
            queue.append(a)
            visited[a] = True
    
for i in range(2,N+1):
    print(answer[i])
# 6 => level 2
