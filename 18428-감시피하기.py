import sys
input = sys.stdin.readline
global flag
N = int(input())
board = [list(map(str, input().split())) for _ in range(N)]
flag = False

def bfs():
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    for t in teachers:# 선생님의 위치에서
        for k in range(4): # 상/하/좌/우 탐색
            nx, ny = t
            
            while 0 <= nx < N and 0 <= ny < N:
                if board[ny][nx] == "O":
                    break

                # 학생이 보이면 실패
                if board[ny][nx] == "S":
                    return False

                nx += dx[k]
                ny += dy[k]
    # 모두 통과하면 학생이 안보이는 것으로 성공
    return True



def bt(depth):
    global flag
    if depth == 3:
        if bfs() == True:
            flag=True
        return
    for i in range(N):
        for j in range(N):
            if board[i][j] =='X':
                board[i][j] = 'O'
                bt(depth+1)
                board[i][j] = 'X'

students = []
teachers = []
for i in range(N):
    for j in range(N):
        if board[i][j] == 'S':
            students.append((j,i))
        elif board[i][j] == 'T':
            teachers.append([j,i])
bt(0)
if flag:
    print("YES")
else:
    print("NO")