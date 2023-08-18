import sys
input = sys.stdin.readline

H, W = map(int, input().split(' '))
world = list(map(int, input().split(' ')))

total = 0
for idx in range(1,W-1):
    leftmax = max(world[:idx])
    rightmax = max(world[idx+1:])

    comp = min(leftmax,rightmax)
    if world[idx] < comp:
        total += comp - world[idx]

print(total)