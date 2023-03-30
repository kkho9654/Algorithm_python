import sys

def jump(n):
    board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    dp_board = [[0 for j in range(n)] for i in range(n)]
    dp_board[0][0] = 1
    for i in range(n):
        for j in range(n):
            move = board[i][j]
            current = dp_board[i][j]
            if i == n-1 and j == n-1:
                print(dp_board[n-1][n-1])
                return
            if i+move < n:
                dp_board[i+move][j] += current
                # if i+move == n-1 and j == n-1:
                    # print(i,j)
            if j+move < n:
                dp_board[i][j+move] += current
                # if i == n-1 and j+move == n-1:
                    # print(i,j)
    # print(dp_board)
    
if __name__ == '__main__':
    jump(int(sys.stdin.readline()))