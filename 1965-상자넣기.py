import sys

N = int(sys.stdin.readline())
cube = list(map(int,sys.stdin.readline().split(' ')))
dp = [1 for _ in range(N)]

for i in range(1, N):
    tmp = []
    for k in range(i):
        if cube[k] < cube[i]:
            tmp.append(dp[k])
    if len(tmp) == 0:
        continue
    dp[i] += max(tmp)
       
print(max(dp))
