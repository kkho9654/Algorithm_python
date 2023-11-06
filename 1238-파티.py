import sys, heapq

input = sys.stdin.readline
INF = int(10e9)

N, M, X = map(int, input().strip().split())
graph = [[]for _ in range(N+1)]
dist = [INF] * (N+1)
for i in range(M):
	s,f,c = map(int, input().strip().split())
	graph[s].append((f,c))

def dijkstra(start):
	# 우선순위 큐 선언
	pq = []
	# start의 dist 0으로 초기화
	dist[start] = 0

	heapq.heappush(pq, (dist[start],start))
	while pq:
		distance, node = heapq.heappop(pq)

		if distance > dist[node]:
			continue
		
		# 해당 노드를 거쳐서 다른 노드들로 갔을 때 비용과 최소비용을 비교하여(더작으면)업데이트 해준다.
		for neighbor in graph[node]:
			neighbor_node, neighbor_distance = neighbor
		
			# 최소거리의 노드를 거쳤을 때가 더 작으면 업데이트 한다. 
			if dist[neighbor_node] > dist[node] + neighbor_distance:
				# 이 때 업데이트 된 놈을 힙큐에 다시 넣는다
				heapq.heappush(pq,(dist[node] + neighbor_distance, neighbor_node))
				dist[neighbor_node] = dist[node] + neighbor_distance

def dijkstra1(start, finish):
	dist = [INF] * (N+1)
	
	# 우선순위 큐 선언
	pq = []
	# start의 dist 0으로 초기화
	dist[start] = 0
	heapq.heappush(pq, (dist[start],start))
	
	while pq:
		distance, node = heapq.heappop(pq)
		if finish == node:
			return dist[node]
		if distance > dist[node]:
			continue
		
		# 해당 노드를 거쳐서 다른 노드들로 갔을 때 비용과 최소비용을 비교하여(더작으면)업데이트 해준다.
		for neighbor in graph[node]:
			neighbor_node, neighbor_distance = neighbor
		
			# 최소거리의 노드를 거쳤을 때가 더 작으면 업데이트 한다. 
			if dist[neighbor_node] > dist[node] + neighbor_distance:
				# 이 때 업데이트 된 놈을 힙큐에 다시 넣는다
				heapq.heappush(pq,(dist[node] + neighbor_distance, neighbor_node))
				dist[neighbor_node] = dist[node] + neighbor_distance

dijkstra(X)
dist1 = dist[:]
ans = []
for i in range(1,N+1):
    if i == X:
        continue
    distance = dijkstra1(i, X)
    ans.append(dist1[i]+distance)

print(max(ans))
	


