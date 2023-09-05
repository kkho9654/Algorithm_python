import sys,heapq
input = sys.stdin.readline
# print = sys.stdout.write
N = int(input())
nums = [int(input()) for _ in range(N)]
heapq.heapify(nums)

ans = 0
while len(nums) > 1:
    a = heapq.heappop(nums)
    b = heapq.heappop(nums)
    heapq.heappush(nums, a+b)
    ans += a+b

print(ans)