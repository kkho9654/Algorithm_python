import sys
input = sys.stdin.readline

N = int(input())
vip = set()
for i in range(int(input())):
    vip.add(int(input()))
dp = [0]* (N+2)
dp[0] = 1
dp[1] = 1
dp[2] = 2

mx = 0
tmp = 0
arr = []
for i in range(1,N+1):
    if i in vip:
        arr.append(tmp)
        mx = max(mx,tmp)
        tmp = 0
    else:
        tmp+=1
mx = max(mx,tmp)
arr.append(tmp)

for i in range(3,mx+1):
    dp[i] = dp[i-1]+ dp[i-2]
ans = dp[arr[0]]
for idx in range(1,len(arr)):
    ans*=dp[arr[idx]]
print(ans)
