import sys
from collections import deque
input = sys.stdin.readline

def bfs(start, end):
    queue = deque([])
    visited = set()

    queue.append((start, 0))
    visited.add(start)
    mn = 10000001

    while queue:
        cur, depth = queue.popleft()
        if cur == end:
            return depth
        tmp = cur
        while tmp!= 0 and tmp < end:
            tmp = 2*tmp
            flag = True
            if tmp == end:
                return depth
            if tmp > end:
                if tmp < mn:
                    mn = tmp
                else:
                    flag = False
            if flag == True and tmp not in visited:
                visited.add(tmp)
                queue.append((tmp,  depth))
        if cur - 1 == end:
            return depth + 1
        if cur + 1 == end:
            return depth + 1
        if cur - 1 >= 0 and cur - 1 not in visited:
            visited.add(cur - 1)
            queue.append((cur - 1, depth+1))
        if cur + 1 not in visited:
            visited.add(cur + 1)
            queue.append((cur + 1, depth+1))

start, end = list(map(int,input().strip().split()))
print(bfs(start, end))