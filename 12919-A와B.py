import sys

S = sys.stdin.readline()[:-1]
T = sys.stdin.readline()[:-1]

def addA(S, T):
    print(S, T)
    if check(S,T):
        S+= 'A'
        addA(S, T)
        addB(S, T)
    else:
        print('asdasd')
        if S==T:
            print(1)
            exit()
        else:
            return

def addB(S, T):
    print(S, T)
    if check(S,T):
        S += 'B'
        list_s = list(S)
        list_s.reverse()
        S = "".join(list_s)
        addA(S, T)
        addB(S, T)
    else:
        # print('asdasd')
        if S==T:
            print(1)
            exit()
        else:
            return

def str_AB_length(str):
    total_length = len(str) - 1
    count = 0
    for t in str:
        if t=='A':
            count+=1
    countA = count
    countB = total_length - count
    return countA, countB
def check(S,T):
    sa, sb = str_AB_length(S)
    ta, tb = str_AB_length(T)
    print(sa, sb, ta, tb)
    if sa >= ta or sb >= tb:
        return False
    else:
        return True
def checkB(S,T):
    sa, sb = str_AB_length(S)
    ta, tb = str_AB_length(T)
    if sb > tb:
        return False
    else:
        return True

if __name__ == '__main__':
    addA(S,T)
    addB(S,T)
    print(-1)
