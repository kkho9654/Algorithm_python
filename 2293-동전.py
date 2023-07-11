import sys

n, k = map(int,sys.stdin.readline().split(' '))
coin = []
for _ in range(n):
    coin.append(int(sys.stdin.readline()))

dp = [0 for _ in range(k)]


for c in (sorted(coin)): 
    for i in range(k):
        if i == c-1:
            dp[i] += 1
        if i-c >= 0 :
            dp[i] += dp[i-c]

print(dp)
print(dp[k-1])
