import sys, collections
input = sys.stdin.readline
sys.setrecursionlimit(10000000)

global F,G,U,D
F,S,G,U,D = list(map(int,input().split()))
def bfs(start):
    queue = collections.deque([(start,0)])
    visited = set()
    while queue:
        # print(queue)
        current, depth = queue.popleft()
        if current in visited:
            continue
        visited.add(current)
        if current == G:
            print(depth)
            exit()
        up = current + U
        down = current - D
        if up <= F:
            queue.append((up,depth+1))
        if down >=1:
            queue.append((down,depth+1))

bfs(S)
print('use the stairs')