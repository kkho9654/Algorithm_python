import sys

inp = sys.stdin.readline()[:-1]
global min
max = -100000000
min = 100000000
num = 0

def search(inp, num):
    global max, min
    # print("input = ",inp)
    for i in inp:
        if int(i)%2 != 0:
            num += 1
    # print(num)
    if len(inp) == 1:
        if num < min :
            min = num
        if num > max :
            max = num
        return
    elif len(inp) == 2:
        search(str(int(inp[0:1])+int(inp[1:2])),num)
    else:
        for i in range(1, len(inp)):
            for j in range(i+1,len(inp)):
                search(str(int(inp[0:i])+ int(inp[i:j])+ int(inp[j:])), num)
                # search(inp[i:j], num)
                # search(inp[j:], num)
                
               
search(inp,0)
print(min,max)

    
    