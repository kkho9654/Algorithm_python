import sys
from collections import deque

graph = {
    1: [2, 4],
    2: [3],
    3: [6],
    4: [5],
    5: [7, 8],
    6: [3],
    7: [5],
    8: [5]
}


def bfs(start):
    queue = deque([]) 
    visited = {}
    depth = 0
    # 시작 노드 넣는다.
    queue.append(start)

    # 시작 노드에 대해 방문 처리
    visited[start] = depth

    while queue:
        # 2. 현
        cur = queue.popleft()
        depth += 1
        print(cur)
        # graph[x]는 x의 인접한 노드들이 담겨있다.
        for neighbor in graph[cur]:
            # 인접한 노드가 방문한 노드가 아닐 때만 큐에 넣어준다.
            if neighbor not in visited:
                queue.append(neighbor)
                visited[cur] = depth

bfs(1)
