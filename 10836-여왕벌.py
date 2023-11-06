import sys

# 애벌레는 낮 열두시에 성장
# 0, 1, 2 중 하나로 더 자람
# 0 행, 0 열 은 입력으로 주어짐 왼열밑부터 순서대로 0행 맨 오른쪽까지 순서대로 줌
# 가장 많이 자란 애벌레 만큼 나머지도 성장

N, M = map(int, input().strip().split())

nums = [1] * (2*N - 1)
for i in range(M):
    zero, one, two = list(map(int, input().strip().split()))
    for j in range(zero, zero + one):
        nums[j] += 1
    for j in range(zero + one, 2*N-1):
        nums[j] += 2

# print(nums)
arr = nums[N:2*N - 1]
# print(arr)
for i in range(N-1, -1,-1):
    print(nums[i], end=' ')
    print(*arr)
    
# r ,c, i = N-1, 0, 0
# while c != N :
#     tmp_board[r][c] += nums[i]
#     board[r][c] += nums[i]
#     if r > 0:
#         r -= 1
#     else:
#         c += 1
#     i += 1

# for r in range(1, N):
#     for c in range(1,N):
#         tmp_mx = []
#         if r-1 >= 0:
#             tmp_mx.append(tmp_board[r-1][c])
#         if r-1 >= 0 and c-1 >=0:
#             tmp_mx.append(tmp_board[r-1][c-1])
#         if c-1 >= 0:
#             tmp_mx.append(tmp_board[r][c-1])
#         tmp = max(tmp_mx)
#         tmp_board[r][c] += tmp
#         board[r][c] += tmp
    
# for b in board:
#     print(*b)
