import sys
input = sys.stdin.readline

N = int(input())

top = list(map(int, input().split()))

for i in range(N-1,-1,-1):
    j = i - 1
    top[i]