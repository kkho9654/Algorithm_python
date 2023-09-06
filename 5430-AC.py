import sys, collections
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    ps = input().strip()
    n = int(input().strip())
    tmpinput = input().strip()
    if tmpinput == '[]':
        nums = collections.deque([])
    else:
        try:
            nums = collections.deque(list(map(str,tmpinput.strip().strip('[').strip(']').split(','))))
        except:
            print('error')
            continue
    switch = True
    flag = True

    for p in ps:
        # print(ps,p,nums)
        if p=='R':
            switch = not switch
        else:
            if len(nums) == 0:
                print('error')
                flag = False
                break
            if switch:
                nums.popleft()
            else:
                nums.pop()
    if flag:
        if switch:
            print("["+",".join(list(nums))+"]")
        else:
            tmp = list(nums)
            tmp.reverse()
            print("["+",".join(tmp)+"]")

