import sys

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    arr = list(map(int,sys.stdin.readline().split()))
    if n == 1:
        print(1)
        exit()
    ret = set()
    count_1 = 1
    count_2 = 1
    for idx, x in enumerate(arr):
        if idx>0:
            if arr[idx] < arr[idx-1]:
                ret.add(count_2)
                count_2 = 1
                count_1 += 1
            elif arr[idx] == arr[idx-1]:
                count_1 += 1
                count_2 += 1
            elif arr[idx] > arr[idx-1]:
                ret.add(count_1)
                count_1 = 1
                count_2 += 1
            else:
                ret.add(count_1)
                ret.add(count_2)
                count_1 = 1
                count_2 = 1
    ret.add(count_1)
    ret.add(count_2)
    print(max(ret))