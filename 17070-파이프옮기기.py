import sys

N = int(sys.stdin.readline())

house = [list(map(int, sys.stdin.readline().split(' '))) for _ in range(N)]

# for i in range(N):
#     print(*house[i])

dp = [[[0 for _ in range(N)] for _ in range(N)] for _ in range(3)]

# 왼쪽에서 오거나 왼쪽위에서오거나 위에서 오는 경우 3가지

dp[0][0][1] = 1
# dp[1][0][1] = 1
# for idx in range(3):
#     print(idx)
#     for i in range(N):
#         print(*dp[idx][i])
# 0=가로 1=대각선 2=세로
# 가로일때는 가로와 대각선의dp참고
# 대각선일 때는 가로와 세로와 대각선의 dp참고
# 세로일때는 세로와 대각선의 dp참고
for i in range(N):
    for j in range(1, N):
        if house[i][j] == 1:
            continue
        if i!=0:
            # 가로
            # print(i, j)
            dp[0][i][j] = dp[0][i][j-1] + dp[1][i][j-1]
            # 대각선
            if house[i-1][j] == 1 or house[i][j-1] == 1:
                pass
            else:
                dp[1][i][j] = dp[0][i-1][j-1] + dp[2][i-1][j-1] + dp[1][i-1][j-1]
            # 세로
            dp[2][i][j] = dp[2][i-1][j] + dp[1][i-1][j]
        else:
            # 가로
            # print(i, j)
            if not (i==0 and j==1):
                dp[0][i][j] = dp[0][i][j-1] + dp[1][i][j-1]
                # 대각선
                # pass
                # 세로
                # dp[2][i][j] = dp[2][i-1][j] + dp[1][i-1][j]

# for idx in range(3):
#     print(idx)
#     for i in range(N):
#         print(*dp[idx][i])
print(dp[0][N-1][N-1]+dp[1][N-1][N-1]+dp[2][N-1][N-1])
                        