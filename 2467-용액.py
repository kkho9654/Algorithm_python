import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
global_min = 2000000002

for idx in range(len(arr)-1):
    start = idx+1
    end = len(arr) - 1
    minimum = 2000000001
    flag = False
    while start<=end:
        mid = (start+end) // 2
        plus = arr[idx] + arr[mid]
        # print(arr[idx], arr[mid],plus)
        
        if plus < 0:
            start = mid + 1
        else:
            end = mid - 1
        if minimum > abs(plus):
            minimum = abs(plus)
            tmp = (arr[idx], arr[mid])
    
    if minimum < global_min:
        global_min = minimum
        ans = tmp

print(*ans)
