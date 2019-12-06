N = int(input())
TravelTimeList = []
StartTimeList = []
WaitTimeList = []
for i in range(N - 1):
    c , s , f = map(int,input().split())
    TravelTimeList.append(c)
    StartTimeList.append(s)
    WaitTimeList.append(f)

sum_val = 0
for i in range(N - 1):
    sum_val = StartTimeList[i] + TravelTimeList[i]
    for j in range(i + 1 , N - 1):
        sum_val = max(sum_val , StartTimeList[j])
        WaitTime = (WaitTimeList[j] - ((sum_val - StartTimeList[j]) % WaitTimeList[j])) % WaitTimeList[j]
        sum_val += TravelTimeList[j] + WaitTime
    print(sum_val)
print("0")
