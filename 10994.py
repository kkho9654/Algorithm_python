def star(n):
    if n == 1:
        rows = 1
        cols = 1
        arr = [['*' for j in range(cols)] for i in range(rows)]
        return arr
    rows = int(4*n - 3)
    cols = int(4*n - 3)
    arr = [[' ' for j in range(cols)] for i in range(rows)]
    
    prev = star(n-1)

    row_col_size = int(len(prev)) + 4
    for i in range(row_col_size):
        for j in range(row_col_size):
            if i == 0  or i == row_col_size - 1:
                arr[i][j] = '*'
            elif j== 0  or j == row_col_size - 1:
                arr[i][j] = '*'
            elif i >= 2 and i <= 1 + len(prev) and j >= 2 and j <= 1 + len(prev) :
                arr[i][j] = prev[i-2][j-2]
    # print(n,prev)
    # print(n,arr)

    return arr

if __name__ == '__main__':
    arr = star(int(input()))
    # print(arr)
    for i in range(len(arr)):
        for j in range(len(arr)):
            print(arr[i][j], end='')
        print()
