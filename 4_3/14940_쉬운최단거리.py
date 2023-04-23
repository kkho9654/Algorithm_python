import sys

def bfs(map, result, i, j, N, M):
    queue = []
    queue.append((i,j))
    result[i][j] = 0

    while True:
        if len(queue)==0:
            break
        tmp =  queue.pop()
        tmp_i = int(tmp[0])
        tmp_j = int(tmp[1])
        if tmp_i+1 < N and map[tmp_i+1][tmp_j] == 1 and result[tmp_i+1][tmp_j] == -1:
            queue.insert(0, (tmp_i+1,tmp_j))
            result[tmp_i+1][tmp_j] = result[tmp_i][tmp_j] + 1

        if tmp_i-1 >= 0 and map[tmp_i-1][tmp_j] == 1 and result[tmp_i-1][tmp_j] == -1:
            queue.insert(0, (tmp_i-1,tmp_j))
            result[tmp_i-1][tmp_j] = result[tmp_i][tmp_j] + 1

        if tmp_j+1 < M and map[tmp_i][tmp_j+1] == 1 and result[tmp_i][tmp_j+1] == -1:
            queue.insert(0, (tmp_i,tmp_j+1))
            result[tmp_i][tmp_j+1] = result[tmp_i][tmp_j] + 1

        if tmp_j-1 >= 0 and map[tmp_i][tmp_j-1] == 1 and result[tmp_i][tmp_j-1] == -1:
            queue.insert(0, (tmp_i,tmp_j-1))
            result[tmp_i][tmp_j-1] = result[tmp_i][tmp_j] + 1
        # print(queue)


if __name__ == '__main__':
    group_count = 0
    input = list(map(int,sys.stdin.readline().split(' ')))
    N = input[0]
    M = input[1]
    map = [list(map(int,sys.stdin.readline().split(' '))) for _ in range(N)]
    result = [[-1 for _ in range(M)]for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if map[i][j] == 1:
                result[i][j] = -1
            elif map[i][j] == 0:
                result[i][j] = 0
    for i in range(N):
        for j in range(M):
            if map[i][j] == 2:
                bfs(map, result, i, j, N, M)
                break
    for i in range(N):
        print(*result[i])

    # 배열의 총 크기, 배열정렬 후 결과 출력

