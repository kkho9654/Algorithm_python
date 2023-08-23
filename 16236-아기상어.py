import sys,time
from collections import deque
input = sys.stdin.readline

N = int(input())
board = []
shark = None
for i in range(N):
    tmp = list(map(int,input().split()))
    board.append(tmp)
    for idx,t in enumerate(tmp):
        if t == 9:
            shark = (idx,i)

def check_help(board, weight):
    for i in range(N):
        for j in range(N):
            if board[i][j] < weight and board[i][j]!=0 and board[i][j]!=9:
                return True
    return False

dx = [0,-1,1,0]
dy = [-1,0,0,1]

weight = 2
ans = 0
eating_num = 0

while check_help(board, weight):
    queue = deque([(shark,0)])
    visited = set()
    while queue:
        # print(queue)
        pos, depth = queue.popleft()
        x,y = pos
        flag = False
        for i in range(4):
            new_pos_x = x+dx[i]
            new_pos_y = y+dy[i]
            if new_pos_y >= 0 and new_pos_y < N and new_pos_x >= 0 and new_pos_x < N:
                if board[new_pos_y][new_pos_x] <= weight and board[new_pos_y][new_pos_x] != 9:
                    # 지나갈 수만 있는 경우
                    if board[new_pos_y][new_pos_x] == 0 or board[new_pos_y][new_pos_x] == weight:
                        if (new_pos_x,new_pos_y) not in visited:
                            queue.append(((new_pos_x,new_pos_y),depth+1))
                            visited.add((new_pos_x,new_pos_y))
                    # 최단거리의 물고기를 찾은 경우...
                    else:
                        # print(f'weight = {weight}, distance = {depth+1}')
                        eating_num += 1
                        ans += depth+1
                        if weight == eating_num:
                            weight +=1
                            eating_num = 0
                        # weight += board[new_pos_y][new_pos_x]
                        board[new_pos_y][new_pos_x] = 9
                        board[shark[1]][shark[0]] = 0
                        shark = (new_pos_x,new_pos_y)
                        flag = True
                        break
        if flag:
            break
    # for b in board:
    #     print(*b)
    # time.sleep(1)

print(ans)