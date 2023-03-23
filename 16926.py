import copy

def rounding(N,M,A,R):
    minimum = min(N,M)

    arr_k = []
    for k in range(int(minimum/2)):
        tmp = []
        i=k
        j=k
        while True:
            tmp.append(A[i][j])
            if i==k+1 and j == k:
                break
            if j == k and i != k:
                i -= 1
            elif i == N - k - 1:
                j -= 1
            elif j == M - k - 1:
                i += 1
            elif i == k :
                j += 1 

        arr_k.append(copy.deepcopy(tmp))
    for arr in arr_k:
        for r in range(R):
            arr.append(arr[0])
            del arr[0]

    for k in range(int(minimum/2)):
        count = 0
        i=k
        j=k
        while True:
            A[i][j] = arr_k[k][count]
            count += 1
            if i==k+1 and j == k:
                break
            if j == k and i != k:
                i -= 1
            elif i == N - k - 1:
                j -= 1
            elif j == M - k - 1:
                i += 1
            elif i == k :
                j += 1 
    
    return A

if __name__ =='__main__':
    n, m, r = map(int, input().split())
    a = []
    for i in range(n):
        a.append(list(map(int, input().split())))
    result = rounding(n,m,a,r)

    str_ = ''

    for i in range(n):
        if i == n-1:
            str_ += ' '.join(list(map(str,a[i])))
        else:
            str_ += ' '.join(list(map(str,a[i]))) +'\n'
    print(str_,end='')