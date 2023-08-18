import sys
import collections

input = sys.stdin.readline

N = int(input())
arr =list(map(int,input().strip().split(' ')))
delete_node = int(input())

tree = collections.defaultdict(list)

root_ = 0
for idx, parent in enumerate(arr):
    if int(parent) == -1:
        root_ = idx
    tree[idx]
    tree[int(parent)].append(idx)


def search(node, arr):
    arr[node] = -2
    for child in tree[node]:
        search(child,arr)
search(delete_node, arr)
cnt = 0
for i in range(len(arr)):
    if arr[i] != -2 and i not in arr:
        cnt += 1
# print(arr)
# print(tree)
print(cnt)