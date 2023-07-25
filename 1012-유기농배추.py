import sys
sys.setrecursionlimit(3000)

def search(depth, ground, x,y):
    global M,N
    ground[y][x] = 2
    if x+1<M and ground[y][x+1] == 1:
        search(depth+1, ground, x+1,y)
    if y+1<N and ground[y+1][x] == 1:
        search(depth+1, ground, x,y+1)
    if x-1>=0 and ground[y][x-1] == 1:
        search(depth+1, ground, x-1,y)
    if y-1>=0 and ground[y-1][x] == 1:
        search(depth+1, ground, x,y-1)
    # for g in ground:
    #     print(*g)
    # print()
result = []
global M,N

for _ in range(int(sys.stdin.readline())):
    num = 0
    M = 0
    N = 0
    M,N,K = list(map(int,sys.stdin.readline().split(' ')))
    ground = [[0 for _ in range(M)] for _ in range(N)]
    for _ in range(K):
        x,y = list(map(int,sys.stdin.readline().split(' ')))
        ground[y][x] = 1

    for i in range(N):
        for j in range(M):
            if ground[i][j] == 1:
                # print('==================')
                num += 1
                search(0,ground,j,i)

    result.append(num)
    
for r in result:
    print(r)