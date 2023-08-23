import sys,collections
input = sys.stdin.readline

global ans
ans = 0
N = int(input())
numbers = list(map(int,input().split()))
dp = [0]*21
dp[numbers[0]] = 1

for idx, num in enumerate(numbers):
    if idx>0 and idx<N-1:
        # print(idx, dp)
        dp_tmp = [0]*21
        for i, d in enumerate(dp):
            if d>0:
                if i+num <= 20:
                    dp_tmp[i+num] += d
                if i-num >= 0:
                    dp_tmp[i-num] += d
        dp = dp_tmp[:]

print(dp[numbers[N-1]])
# def bt(depth, sum):
#     global ans
#     if depth == N-1:
#         if numbers[N-1] == sum:
#             ans+=1
#         return
    
#     num = numbers[depth]
#     flag = 0
#     if sum+num <= 20:
#         bt(depth+1, sum+num)
#     else:
#         flag+=1
#     if sum-num>=0:
#         bt(depth+1, sum-num)
#     else:
#         flag+=1

#     if flag == 2:
#         return
# bt(0,0)
# print(ans)