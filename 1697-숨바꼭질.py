import sys

N, K = list(map(int,sys.stdin.readline().split(' ')))
m = max(N,K)
dp = [100000 for _ in range(2*m+1)]
dp[N] = 0
for i in range(N-1,-1,-1):
    # print(dp[i+1])
    dp[i] = dp[i+1] + 1
if N<K:
    for i in range(2*m+1):
        if i-1>=0 and dp[i] > dp[i-1] + 1:
            dp[i] = dp[i-1] + 1

        if i+1 < 2*m + 1 and dp[i] > dp[i+1] + 1:
            dp[i] = dp[i+1] + 1

        if i*2<2*m+1 and dp[i*2] > dp[i] + 1:
            dp[i*2] = dp[i] + 1
# print(dp)
print(dp[K])