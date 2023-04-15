import sys

if __name__ == '__main__':
    N = int(sys.stdin.readline())
    if N == 1:
        print(3)
        exit()
    elif N == 2:
        print(7)
        exit()
    D = [[0 for _ in range(2)] for _ in range(N)]
    D[0][1] = 1
    D[0][0] = 3
    D[1][1] = 2
    D[1][0] = 7
    for i in range(1, N):
        D[i][1] = D[i-1][0] - D[i-1][1]
        D[i][0] = (D[i-1][0]+2*(D[i][1]))

    print(D[N-1][0])

# 1	1
# 1+1+1	3 
# 3+(1+1)+(1+1)  7
# 7+(3+2) + (3+2)  17
# 17+(7+5) + (7+5) = 41