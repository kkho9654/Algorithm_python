import sys,collections
deque = collections.deque
input = sys.stdin.readline

N,M = map(int,input().split(' '))
s = {}
for _ in range(N+M):
    x, y = map(int,input().split(' '))
    s[x] = y

queue = deque()
queue.append((1,0))
visited =  set()
while queue:
    cur, depth = queue.popleft()
    if cur == 100:
        print(depth)
        break
    for i in range(1,7):
            if cur+i in s.keys():
                if s[i+cur] not in visited:
                    visited.add(s[i+cur])
                    queue.append((s[i+cur], depth+1))
            else:
                if cur+i not in visited:
                    visited.add(i+cur)
                    queue.append((i+cur, depth+1))