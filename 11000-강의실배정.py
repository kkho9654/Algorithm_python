import sys
input = sys.stdin.readline

N = int(input())
time_table = []
mx = 0
for i in range(N):
    a, b = map(int,input().split())
    mx = max(mx, a, b)
    time_table.append((a,b))
# 끝나는 시간 중 가장 작은거 뽑는다.
# 뽑은 끝나는 시간 보다 작은 시작시간을 센다.