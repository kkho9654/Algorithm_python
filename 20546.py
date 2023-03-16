import copy

def jun(money, stocks):
    stock_quantity = 0
    for idx, stock in enumerate(stocks):
        stock_quantity += money // stock
        money = money % stock

    return money + stocks[13]*stock_quantity

def sung(money, stocks):
    stock_quantity = 0
    for idx in range(len(stocks)):
        if idx >= 3:
            # 상승
            if stocks[idx] > stocks[idx-1] and stocks[idx-1] > stocks[idx-2] and stocks[idx-2] > stocks[idx-3]:
                money += stock_quantity * stocks[idx]
                stock_quantity = 0
            elif stocks[idx] < stocks[idx-1] and stocks[idx-1] < stocks[idx-2] and stocks[idx-2] < stocks[idx-3]:
                stock_quantity += money // stocks[idx]
                money = money % stocks[idx]
            
    return money + stocks[13]*stock_quantity

if __name__ == '__main__':
    money = int(input())
    stocks_input = input()
    stocks_str = stocks_input.split(' ')
    stocks = [int(x) for x in stocks_str]

    jun_money = jun(money, copy.deepcopy(stocks))
    sung_money = sung(money, copy.deepcopy(stocks))
    if jun_money > sung_money:
        print('BNP')
    elif jun_money < sung_money:
        print('TIMING')
    else:
        print('SAMESAME')