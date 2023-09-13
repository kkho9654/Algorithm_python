import sys, collections
input = sys.stdin.readline

N = int(input())
nums = list(map(int,input().strip().split()))
# 배열 왼쪽으로 한칸씩 쉬프트
stack = []
ans = [-1]* N
for i in range(N):
    while stack and (stack[-1][0] < nums[i]):
        data, idx = stack.pop()
        ans[idx] = nums[i]
    stack.append([nums[i],i])
print(*ans)
