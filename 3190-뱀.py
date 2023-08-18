import sys
import collections
input = sys.stdin.readline

N = int(input())
K = int(input())

board = [[0 for _ in range(N)] for _ in range(N)]

for _ in range(K):
    row, col = list(map(int,input().rstrip().split(' ')))
    board[row-1][col-1] = 2
board[0][0] = 1

L = int(input())
change_d = {}
for _ in range(L):
    X, C = input().rstrip().split(' ')
    change_d[int(X)] = C
time = 0
state = 0
x,y = (0,0)
tail_x, tail_y = 0,0
directions = [(1,0), (0,1), (-1, 0), (0,-1)]
bams = collections.deque()

bams.append((x,y))
while True:
    d_x, d_y = directions[state]
    # 벽
    if y+d_y<N and x+d_x<N and y+d_y>=0 and x+d_x>=0:
        # 자기자신
        if board[y + d_y][x + d_x] != 1:
            new_pos_x = x+d_x
            new_pos_y = y+d_y
            bams.append((new_pos_x , new_pos_y))
            if board[new_pos_y][new_pos_x] != 2:
                # print('pop left!')
                tmpx,tmpy = bams.popleft()
                board[tmpy][tmpx] = 0
            board[new_pos_y][new_pos_x] = 1
        else:
            break
    else:
        break

    x = x + d_x
    y = y + d_y
    time+=1

    try:
        if change_d[time] == 'L':
            state -= 1
            if state == -1:
                state = 3
        elif change_d[time] == 'D':
            # print(time)
            state += 1
            if state == 4:
                state = 0
    except:
        pass
print(time+1)
