import sys
import copy
from _heapq import _heappop_max, _heapify_max, _heapreplace_max

N = int(sys.stdin.readline())

table = [list(map(int,sys.stdin.readline().split(' '))) for _ in range(N)]

line2 = [N - 2 for _ in range(5)]
table_2 = copy.deepcopy(table[N-2])
table_1 = copy.deepcopy(table[N-1])
for _ in range(N-1):
    # 두번째 줄의 max의 index
    line2_max = max(table_2)
    index_max = table_2.index(line2_max)

    # 첫번째 줄의 min의 index
    line1_min = min(table_1)
    index_min = table_1.index(line1_min)
    
    # 첫번재 줄의 min과 두번째 줄의 max를 비교
    if line2_max > line1_min:
        table_1[index_min] = line2_max
        line2[index_max] -= 1
        table_2[index_max] = table[line2[index_max]][index_max]
    else:
        break
print(min(table_1))
