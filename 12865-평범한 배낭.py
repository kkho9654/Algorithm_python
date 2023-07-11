import sys

N, K = map(int, sys.stdin.readline().split(' '))

wv = [tuple(map(int, sys.stdin.readline().split(' '))) for _ in range(N)]
dp = [[0 for _ in range(K+1)] for _ in range(N+1)]
wv.sort(key = lambda x:  x[0])

for k in range(N):
    w = wv[k][0]
    v = wv[k][1]
    for i in range(K+1):
        if i - w >= 0:
            if dp[k][i-w] + v >= dp[k][i]:
                dp[k+1][i] = dp[k][i-w] + v
            else:
                dp[k+1][i] = dp[k][i]
        else:
            dp[k+1][i] = dp[k][i]
    # print(dp[k])
# print(dp[N])
print(max(dp[N]))

'''
https://gsmesie692.tistory.com/113
ㅁdp를 1차원으로 하면 생기는 문제... 보석이 하나씩 돌 때 현재 보석의 i무게일 때 최적의 값은 
[i-w의 value + 현재 보석의 V] or [이전 보석의 i의 value] 인데
1차원으로 하면i-w의 value가 갱신이 되버려서 중복으로 계속 들어갈 수가 있다.
'''
# 