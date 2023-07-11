import sys

def plus(x,y):
    return x+y
def minus(x,y):
    return x-y
def split(x,y):
    if x < 0 or y<0:
        return -(abs(x)//abs(y))
    return x//y
def multiply(x,y):
    return x*y

operator = []
global max , min
max = -1000000000
min = 1000000000
opmap = {
    "+":plus,
    "-":minus,
    "×":multiply,
    "÷":split,
}

N = int(sys.stdin.readline())
arr = list(map(int,sys.stdin.readline().split(' ')))
oparr = list(map(int,sys.stdin.readline().split(' ')))
tmp = ["+","-","×","÷"]
for idx,opn in enumerate(oparr):
    for i in range(opn):
        operator.append(tmp[idx])

def calculate(depth, x, y,operator):
    global max,min

    if depth == N-2:
        result = opmap[operator.pop()](x,y)
        if result > max:
            max = result
        if result < min:
            min = result
        return
    op_size = len(operator)

    for i in range(op_size):
        tmp = operator[:]
        result = opmap[tmp[i]](x,y)
        del tmp[i]
        # print(depth,result)
        
        calculate(depth+1, result, arr[depth+2],tmp)

calculate(0,arr[0],arr[1],operator)
# print(f'max = {max} , min = {min}')
print(max)
print(min)