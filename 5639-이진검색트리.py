import sys, time
input = sys.stdin.readline
sys.setrecursionlimit(1000000)
arr = []
for line in sys.stdin:
    try:
        arr.append(int(line))
    except:
        break
# print(arr)
tree = {}
def trees(root,arr,tree):
    left = []
    right = []
    lflag = True
    rflag = True
    lroot = -1
    rroot = -1
    for a in arr:
        if a < root:
            if lflag:
                lroot = a
                lflag = False
            left.append(a)
            
        elif a > root:
            if rflag:
                rroot = a
                rflag = False
            right.append(a)
    # print(f'lroot = {lroot} :{left}')
    # print(f'rroot = {rroot} :{right}')
    tree[root] = []
    if lroot != -1:
        tree[root].append(lroot)
    if rroot != -1:
        tree[root].append(rroot)
    if len(left) <= 1 and len(right) <= 1:
        return
    if len(left) <= 1 and len(right) > 1:
        trees(rroot,right,tree)
    if len(right) <= 1 and len(left) > 1:
        trees(lroot,left,tree)
    if len(right) > 1 and len(left) > 1:
        trees(rroot,right,tree)
        trees(lroot,left,tree)

trees(arr[0],arr,tree)
# print(tree)
def post(root):
    try:
        tree[root]
    except:
        print(root)
        return
    for child in tree[root]:
        post(child)
    print(root)
post(arr[0])