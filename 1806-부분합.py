import sys
input = sys.stdin.readline

N, S = map(int,input().split())
nums = list(map(int,input().split()))

mn = sys.maxsize
dp = [0]*(N+1)
for idx in range(1,N+1):
    dp[idx] += dp[idx-1] + nums[idx-1]

# S보다 커질때까지 r포인터 오른쪽으로 움직이기
l = 0
r = 0
while r < N+1:
    if dp[r] - dp[l] >= S:
        mn = min(mn, r-l)
        l += 1
    else:
        r += 1
        
if l == 0:
    print(0)
else:
    print(mn)

