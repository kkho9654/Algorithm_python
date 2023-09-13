import sys, heapq
input = sys.stdin.readline
global ans
def firstOrd(string,shift):
    if string == '':
        return
    arr = []
    for i, s in enumerate(string):
        heapq.heappush(arr, (ord(s), i))
    ords, idx = heapq.heappop(arr)

    ans[idx+shift] = chr(ords)
    print(''.join(ans))
    firstOrd(string[idx+1:], shift+idx+1)

    firstOrd(string[:idx], shift)

# ord가 가장 낮은 문자를 찾는다. 앞 뒤로 나뉘는데 뒤에부분에서 해당 함수 실행
string = input().strip()
ans = [''] * len(string)

firstOrd(string,0)
