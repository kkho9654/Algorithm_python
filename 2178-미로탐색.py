import sys,collections
input = sys.stdin.readline

N, M = map(int,input().split(' '))
maze = [list(map(int,input()[:-1])) for _ in range(N)]

queue = collections.deque()
visisted = set()
queue.append((0,0,0))
depth = 0
arr1 = [1, -1,0,0]
arr2 = [0,0,1, -1]
visisted.add((0,0))
while queue:
    x, y, depth = queue.popleft()
    if x == M-1 and y == N-1:
        print(depth+1)
        break
    for i in range(4):
        newpos_x = x+arr1[i]
        newpos_y = y+arr2[i]
        if newpos_x >= 0 and newpos_y>=0 and newpos_x<M and newpos_y<N:
            if maze[newpos_y][newpos_x] == 1 and (newpos_x,newpos_y) not in visisted:
                visisted.add((newpos_x,newpos_y))
                queue.append((newpos_x,newpos_y, depth+1))
