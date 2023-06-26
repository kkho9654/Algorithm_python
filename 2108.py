# 20230626

import sys
from collections import defaultdict
import math

if __name__ == '__main__':
    N = int(sys.stdin.readline())

    maxarr = []
    arr = []
    max = 0
    maxdict = defaultdict(int)
    for _ in range(N):
        line = int(sys.stdin.readline())
        arr.append(line)
        maxdict[line]
        maxdict[line] += 1
        if maxdict[line] > max:
            maxarr.clear()
            maxarr.append(line)
            max = maxdict[line]
        elif maxdict[line] == max:
            maxarr.append(line)

    arr = sorted(arr)
    maxarr = sorted(maxarr)
    mean = math.fsum(arr)/N
    if mean > 0:
        print(int(mean+0.5))
    else:
        print(int(mean-0.5))
    print(arr[int(N/2)])
    if len(maxarr) > 1:
        print(maxarr[1])
    else:
        print(maxarr[0])
    print(arr[len(arr)-1] - arr[0])