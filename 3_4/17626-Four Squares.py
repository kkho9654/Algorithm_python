import time

def squares(n):
    arr = [0 for i in range(n+1)]
    
    arr[1] = 1
    if n>1:
        arr[2] = 2
        arr[3] = 3
    square = 1
    
    for i in range(n+1):
        if i>1:
            pprev_val = (square-2)**2
            prev_val = (square-1)**2
            current_val = square**2
            next_val = (square+1)**2
            if next_val == i:
                square += 1
                arr[i] = 1
            else:
                compare1 = arr[current_val] + arr[i-current_val]
                compare2 = arr[prev_val] + arr[i - prev_val]
                compare3 = arr[pprev_val] + arr[i - pprev_val]
                minimum = min(compare2,compare1,compare3)
                arr[i] = minimum
            # print(i, current_val, i- current_val, arr[i])
    print(arr)
    print(arr[n])
        


if __name__ == '__main__':
    squares(int(input()))