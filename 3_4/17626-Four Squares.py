import time

def squares(n):
    arr = [0 for i in range(n+1)]
    
    arr[1] = 1
    # if n>1:
    #     arr[2] = 2
    #     arr[3] = 3
    square = 1
    
    for i in range(n+1):
        if i>1:
            next_val = (square+1)**2
            if next_val == i:
                square += 1
                arr[i] = 1
            else:
                tmp_arr = []
                for j in range(0,square):
                    tmp_arr.append(arr[(square-j)**2]+arr[i-((square-j)**2)])
                    # print(f'index = {i} ::: arr[{(square-j)**2}] = {arr[(square-j)**2]} ,arr[{i-((square-j)**2)}] = {arr[i-((square-j)**2)]}  ')
                # print(tmp_arr, min(tmp_arr))
                arr[i] = min(tmp_arr)
                del tmp_arr
    print(arr[n],end='')

if __name__ == '__main__':
    squares(int(input()))