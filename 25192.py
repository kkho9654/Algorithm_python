# 20230626

import sys

if __name__ == '__main__':
    N = int(sys.stdin.readline())

    sets = set()
    gomgom = 0
    for _ in range(N):
        line = sys.stdin.readline()[:-1]
        if line == 'ENTER':
            sets = set()
        else:
            if line not in sets:
                gomgom = gomgom + 1
            sets.add(line)
            

    print(gomgom)

