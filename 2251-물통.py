import sys,copy

abc = list(map(int,sys.stdin.readline().split()))

abc_max = copy.deepcopy(abc)
abc[0] = 0
abc[1] = 0

ans = []
visited = set()
visited.add(tuple(abc))
def notselected(idx):
    return (idx + 1)%3, (idx + 2)%3

def bt(abc,abc_max,visited):
    a,b,c = abc
    # print(a,b,c)
    if abc[0]==0:
        if abc[2] not in ans:
            ans.append(abc[2])
        else:
            return
    
    for idx, k in enumerate(abc):
        if k>0:
            # 나머지 두개 애들 인덱스
            for ns in notselected(idx):
                tmp = abc[:]
                # idx 를 ns로 부어야됨
                tmp[ns] += abc[idx]

                # 부어지는 놈(ns)이 꽉찬경우
                if tmp[ns] > abc_max[ns]: 
                    m =  tmp[ns] - abc_max[ns]
                    tmp[idx] = m
                    tmp[ns] = abc_max[ns]
                else:
                    tmp[idx] = 0
                
                # visited 여부 검사
                if tuple(tmp) not in visited:
                    visited.add(tuple(tmp))
                    bt(tmp,abc_max,visited)

bt(abc,abc_max,visited)
print(*sorted(ans))


    
