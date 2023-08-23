import sys, collections
input = sys.stdin.readline
N = int(input())

max_dp = [0]*3
max_tmp = [0]*3

min_dp = [0]*3
min_tmp = [0]*3

for _ in range(N):
    a,b,c = list(map(int, input().split()))
    for i in range(3):
        if i == 0:
            min_tmp[i] = a + min(min_dp[i],min_dp[i+1])
            max_tmp[i] = a + max(max_dp[i],max_dp[i+1])
        elif i == 1:
            min_tmp[i] = b + min(min_dp[i-1],min_dp[i],min_dp[i+1])
            max_tmp[i] = b + max(max_dp[i-1],max_dp[i],max_dp[i+1])
        elif i == 2:
            min_tmp[i] = c + min(min_dp[i],min_dp[i-1])
            max_tmp[i] = c + max(max_dp[i],max_dp[i-1])
    
    for i in range(3):
        min_dp[i] = min_tmp[i]
        max_dp[i] = max_tmp[i]

print(max(max_dp), min(min_dp))