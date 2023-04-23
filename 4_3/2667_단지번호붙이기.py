import sys

def bfs(map, result, i, j, N):
    # 4방향 확인 
    # 4방향중 1이고 result가 false인거만 queue에 집어넣음
    queue = []
    count = 1
    queue.append((i,j))
    result[i][j] = True

    while True:
        if len(queue)==0:
            break
        tmp =  queue.pop()
        tmp_i = int(tmp[0])
        tmp_j = int(tmp[1])
        if tmp_i+1 < N and map[tmp_i+1][tmp_j] == '1' and result[tmp_i+1][tmp_j] == False:
                queue.insert(0, (tmp_i+1,tmp_j))
                result[tmp_i+1][tmp_j] = True
                count += 1

        if tmp_i-1 >= 0 and map[tmp_i-1][tmp_j] == '1' and result[tmp_i-1][tmp_j] == False:
                queue.insert(0, (tmp_i-1,tmp_j))
                result[tmp_i-1][tmp_j] = True
                count += 1

        if tmp_j+1 < N and map[tmp_i][tmp_j+1] == '1' and result[tmp_i][tmp_j+1] == False:
                queue.insert(0, (tmp_i,tmp_j+1))
                result[tmp_i][tmp_j+1] = True
                count += 1

        if tmp_j-1 >= 0 and map[tmp_i][tmp_j-1] == '1' and result[tmp_i][tmp_j-1] == False:
                queue.insert(0, (tmp_i,tmp_j-1))
                result[tmp_i][tmp_j-1] = True
                count += 1
        # print(queue)
    return count


if __name__ == '__main__':
    group_count = 0
    N = int(sys.stdin.readline())
    map = [list(map(str,sys.stdin.readline())) for _ in range(N)]
    result = [[False for _ in range(N)]for _ in range(N)]
    ret_arr = []
    # print(map,result)
    # map 1인데 result에 아무것도 없을 때  해당부분부터 탐색 시작 탐색한부분 result에 True로 마킹,탐색횟수 배열에 저장
    # map이 0이거나 result에 값이 있으면 탐색안함

    for i in range(N):
        for j in range(N):
            if map[i][j] == '1' and result[i][j] == False:
                ret_arr.append(bfs(map, result, i, j, N))
            else:
                pass

    # 배열의 총 크기, 배열정렬 후 결과 출력
    
    print(len(ret_arr))
    ret_arr.sort()
    try:
        for ret in ret_arr:
            print(ret)
    except:
        pass
