import sys

input = sys.stdin.readline

N = int(input())
nums = map(int, input().strip().split())
M = int(input())

for i in range(N):
    for j in range(i+1, N):
        

for i in range(M):
    s, e = map(int, input().strip().split())
    print(s,e)