import sys, copy

def search(depth, visitied):
    global N,count
    if depth == N - 1:
        # print(visitied)
        count+=1
    
    for i in range(N):
        new_pos = (i,depth+1)
        flag = False
        for x,y in visitied:
            if x == new_pos[0] or y == new_pos[1] or abs(new_pos[1] - y) == abs(new_pos[0] - x):
                flag = True
                break
        if flag is False:
            tmp = set(visitied)
            tmp.add(new_pos)
            # print(tmp)
            # visitied.add(new_pos)
            search(depth + 1, tmp)
            
        
global N, count
N = int(sys.stdin.readline())
count = 0
depth = 0

for i in range(N):
    visitied = set()
    visitied.add((i,0))
    search(0, visitied)
print(count)
