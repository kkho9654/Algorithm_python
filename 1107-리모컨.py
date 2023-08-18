import sys,time

input = sys.stdin.readline

global arr, N
N = int(input())
mn = int(input())

if  mn != 0:
    M = list(map(int,input().split(' ')))
else:
    print(min(len(str(N)),abs(N-100)))
    exit(0)
number = []
a = set(M)
for i in range(10):
    if i not in a:
        number.append(i)
if mn == 10:
    print(abs(N-100))
    exit(0)
arr = []

def bt(depth,ret, number):
    global arr, N
    arr.append(ret)

    if depth==len(str(N)):
        return
    tmp = ret
    for num in number:
        ret *= 10
        ret += num
        bt(depth+1 ,ret, number)
        ret = tmp
for num in number:
    bt(0,num,number)
arr.sort()
print(arr)
# mid = len(arr) // 2
# start= 0 
# end = len(arr) - 1
# arr.sort()
# while mid < end and mid > start:
#     if arr[mid] == N:
#         break
#     if arr[mid] < N:
#         start = mid
#         mid = (end + start) // 2
#     else:
#         end = mid
#         mid = (end + start) // 2
    # print(start, mid, end)
tttmp = 1000000000
x = 0
for a in arr:
    if tttmp > abs(N-a):
        tttmp = abs(N-a)
        x=a
# print(tttmp)
# print(arr[start], arr[mid], arr[end])

# ans = min(abs(N - arr[start]), abs(N - arr[mid]), abs(N - arr[end]))
print(x)
ans = tttmp+len(str(x))
ans = min(ans, abs(N-100))
print(ans)