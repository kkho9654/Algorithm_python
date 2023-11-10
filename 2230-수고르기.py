import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split())
nums = []
for i in range(N):
    nums.append(int(input().strip()))

nums.sort()

first = 0
second = 1
mn = 2000000001
while first<second:
    if nums[second] - nums[first] < M:
        second += 1
    else:
        while nums[second] - nums[first] >= M:
            mn = min(mn, nums[second] - nums[first])
            first += 1
        
    if second > len(nums) - 1:
        break
        
print(mn)