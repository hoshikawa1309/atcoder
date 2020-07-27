N = int(input())
stocks = list(map(int,input().split()))
now_stock = stocks[0]
cash = 1000
max_min_stocks = []
if now_stock <= stocks[1]:
    up_flag = True
    max_min_stocks.append(stocks[0])
else:
    up_flag = False
f_up_flag = up_flag
i = 1

while i < N:
    next_stock = stocks[i]
    if up_flag:
        if now_stock <= next_stock:
            now_stock = next_stock
        else:
            max_min_stocks.append(now_stock)
            up_flag = False
    else:
        if now_stock >= next_stock:
            now_stock = next_stock
        else:
            max_min_stocks.append(now_stock)
            up_flag = True
    now_stock = next_stock
    i += 1
if up_flag:
    max_min_stocks.append(stocks[-1])
else:
    max_min_stocks.append(stocks[-1])
# print(max_min_stocks)

if len(max_min_stocks) >= 2:
    for i in range(len(max_min_stocks) // 2):
        hold_stocks = cash // max_min_stocks[2 * i]
        cash -= hold_stocks * max_min_stocks[2 * i]
        cash += hold_stocks * max_min_stocks[2 * i + 1]
print(cash)


