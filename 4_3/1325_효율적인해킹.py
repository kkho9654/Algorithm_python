from collections import defaultdict
import sys

def bfs(mapping, start, visited):
    count = 1
    queue = []
    queue.append(start)
    dfs_visited = set()
    visited.add(start)
    while True:
        if len(queue) == 0:
            break
        current = queue.pop()
        tmp_list = mapping[current]
        for tmp in tmp_list:
            if tmp not in dfs_visited:
                visited.add(tmp)
                dfs_visited.add(tmp)
                queue.insert(0,tmp)
                count += 1

    return count

if __name__ == '__main__':
    input = list(map(int,sys.stdin.readline().split(' ')))
    N = input[0]
    M = input[1]

    mapping = defaultdict(list)
    freinds = []

    for i in range(M):
        tmp = list(map(int,sys.stdin.readline().split(' ')))
        mapping[tmp[1]].append(tmp[0])
        flag = True
        if tmp[1] in mapping[tmp[0]]:
            for group in freinds:
                if tmp[1] in group or tmp[0] in group:
                    group.add(tmp[1])
                    group.add(tmp[0])
                    flag = False
                    break
            if flag:
                tmp_group = set()
                tmp_group.add(tmp[1])
                tmp_group.add(tmp[0])
                freinds.append(tmp_group)

    ret_arr = []
    max = -1
    visited = set()
    for i in range(1,N+1):
        if i not in visited:
            tmp = bfs(mapping, i, visited)
            # print(i, tmp,max, visited)
            if tmp > max:
                max = tmp
                ret_arr = []
                ret_arr.append(i)
            elif tmp == max:
                ret_arr.append(i)
            else:
                pass

    ret_set = set() 
    for val in ret_arr:
        for group in freinds:
            if val in group:
                ret_set.update(group)
        ret_set.add(val)

    print(*sorted(ret_set))