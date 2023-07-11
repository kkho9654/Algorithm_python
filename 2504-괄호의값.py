import sys
# 상위 depth의 계산에 사용되면 그 밑에 depth는 초기화
if __name__ == '__main__':
    input = sys.stdin.readline()[:-1]
    stack = []
    depth = 0
    ret = [0 for _ in range(31)]

    sdict = {
        '(' : 2,
        '[' : 3,
    }
    valid = {
        '(' : 0,
        '[' : 0,
        ')' : 0,
        ']' : 0,
    }
    before = ''
    for s in input:
        valid[s] += 1
        
        if s == '(' or s == '[':
            stack.append(s)
            depth += 1
            before = s
        else:
            if (s == ')' and before == '[') or (s == ']' and before == '('):
                print(0)
                exit()
            if len(stack) == 0:
                print(0)
                exit()
            depth -= 1
            value = sdict[stack.pop()]

            if ret[depth + 1] > 0:
                value *= ret[depth + 1]
                ret[depth + 1] = 0
            
            old_val = ret[depth]
            del ret[depth]
            ret.insert(depth,old_val + value)
            before = s
    
    if len(stack) != 0 or valid['('] != valid[')'] or valid['['] != valid[']']:
        print(0)
        exit()
    else:
        print(ret[0])

    