import sys
# 1, 2, 5, 7
if __name__ == '__main__':
    price = int(sys.stdin.readline())
    d = [i for i in range(price+1)]
    d.insert(1,1)
    d.insert(2,1)
    d.insert(3,2)
    d.insert(4,2)
    d.insert(5,1)
    d.insert(6,2)
    d.insert(7,1)

    try:
        for idx in range(8, price+1):
            d[idx] = min(d[idx-7],d[idx-5],d[idx-2])+1
    except:
        pass

    print(d[price])
  
