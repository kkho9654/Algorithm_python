import sys, copy
from itertools import combinations 

N = int(sys.stdin.readline())
S = [list(map(int,sys.stdin.readline().split(' '))) for _ in range(N)]
visit = [False for _ in range(N)]
global min_sum
total_set = set()
team_start = set()
min_sum = 10000000
total_arr = set()
for i in range(N):
    total_set.add(i)

def cal_sum(input_list):
    sum = 0
    for i in range(len(input_list)):
        for j in range(i+1,len(input_list)):
            sum+=S[input_list[i]][input_list[j]]
            sum+=S[input_list[j]][input_list[i]]
    return sum

def backtracking(depth):
    global min_sum
    if depth == N/2 :
        team_link = total_set - team_start
        # str = f'{team_start}'
        # total_arr.add(str)

        # if f'{team_link}' in total_arr:
        sum_s = cal_sum(list(team_start))
        sum_l = cal_sum(list(team_link))
        if abs(sum_s- sum_l) < min_sum:
            min_sum = abs(sum_s- sum_l)
        return
    for i in range(depth, N):
        # if i not in team_start:
        if visit[i] == False:
            team_start.add(i)
            visit[i] = True
            backtracking(depth + 1)
            team_start.remove(i)
            visit[i] = False

import time
s = time.time()
backtracking(0)
print(time.time()- s)

# print(total_arr)
print(min_sum)

