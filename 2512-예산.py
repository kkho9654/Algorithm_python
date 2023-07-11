import sys,time

n = int(sys.stdin.readline())
lis= list(map(int,sys.stdin.readline().split(' ')))
m= int(sys.stdin.readline())

start = 0
end = max(lis)
lis.sort()

v = (start + end) // 2

while start <= end :
    sum_list = [i if i<=v else v for i in lis]
    total = sum(sum_list) 
    # print(v, total, start, end)
    if total > m :
        end = v - 1
        v = (start + end) // 2
    elif total < m : 
        start = v+1
        v = (start + end) // 2
    else:
        break
print(v)