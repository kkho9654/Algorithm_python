import sys

n, k = map(int,sys.stdin.readline().split(' '))
coins = [int(sys.stdin.readline()) for _ in range(n)]

dp = [1000000000 for _ in range(k+1)]
dp[0] = 0
coins.sort()
for coin in coins:
    for i in range(coin, k+1):
        if dp[i-coin] + 1 <= dp[i]:
            dp[i] = dp[i-coin] + 1 

print(dp[k] if dp[k]!=1000000000 else -1)
