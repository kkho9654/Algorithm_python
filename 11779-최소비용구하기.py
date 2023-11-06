import sys, heapq

input = sys.stdin.readline
INF = int(10e9)

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]

for i in range(m):
    s,f,c = list(map(int, input().strip().split()))
    graph[s].append((f,c))
start, finish = map(int, input().strip().split()) 

dist = [(INF, -1)] * (n+1)
pq = []
path = []
def dijkstra(start, finish):
    dist[start] = (0,0)
    heapq.heappush(pq, (0,start,0))

    while pq:
        distance, current, origin = heapq.heappop(pq)
        if current == finish:
            break

        if distance > dist[current][0]:
            continue

        for neighbor in graph[current]:
            neighbor_node, neighbor_dist = neighbor
            new_distance = distance + neighbor_dist
            if new_distance < dist[neighbor_node][0]:
                dist[neighbor_node] = (new_distance, current)
                heapq.heappush(pq, (new_distance, neighbor_node, current))

dijkstra(start, finish)


minimum_cost, before = dist[finish]
path.append(before)
path.append(finish)

while before != start:
    _, before = dist[before]
    path.insert(0,before)

print(minimum_cost)
print(len(path))
print(*path)


