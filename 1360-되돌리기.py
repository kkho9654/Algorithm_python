import sys
input = sys.stdin.readline

def undofunc(time, ch, index):
    for i in range(time- ch ,time):
        if arr[index][0] < i:
            return
        # print(i)
        start = 0
        end = index
        mid = (start + end) // 2
        while start <= end:
            mid = (start + end) // 2
            # print(start, mid, end)
            if arr[mid][0] > i:
                end = mid - 1
            elif arr[mid][0] < i:
                start = mid + 1
            elif arr[mid][0] == i:
                if type(arr[mid][1]) == type(int()):
                    undofunc(arr[mid][0], arr[mid][1], index)
                arr[mid][2] = not arr[mid][2]
                break

N = int(input())
arr = []
for i in range(N):
    func, ch, time = input().strip().split()
    time = int(time)
    if func == 'type':
        arr.append([time, ch, True])
    elif func == 'undo':
        ch = int(ch)
        arr.append([time, ch, True])
        index = len(arr) - 1
        undofunc(time, ch, index)
        

for a in arr:
    if a[2] == True and type(a[1]) != type(int()):
        print(a[1], end="")
print()
            