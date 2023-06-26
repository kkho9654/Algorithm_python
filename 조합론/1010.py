# 20230626

import sys

if __name__ == '__main__':
    T = int(sys.stdin.readline())
    for i in range(T):
        N, M = map(int, sys.stdin.readline().split(' '))
        # M C N , m(m-1)
        p = 1
        for i in range(N):
            p = p * M
            M = M - 1
        
        c = 1
        for i in range(N,0,-1):
            c = c * i
        
        print(p,c)
        print(int(p/c))

    