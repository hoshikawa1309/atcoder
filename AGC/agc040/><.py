from collections import Counter
S = list(input())
now = 0
cnt = 1
num = []
max_val = 0
for i in range(len(S)):
    char = S[i]
    if i == len(S) - 1:
        num.append([char, cnt])
    else:
        if S[i] == S[i + 1]:
            cnt += 1
        else:
            num.append([char , cnt])
            cnt = 1
for i in range(len(num)):
    if num[i][1] > max_val:
        max_val = num[i][1]
        if num[i][0] == "<":
            idx = i
        else:
            idx = i + 1
print(idx)
num2 = [-1] * (len(num) + 1)
num2[idx] = 0
now = 0
sum_val = 0
for i in range(idx - 1,-1,-1):
    if num[i][0] == ">":
        num2[i] = num[i][1] + num2[i + 1]
        sum_val += ((num2[i] + num2[i + 1]) * (num[i][1] + 1)) // 2
    else:
        if i == 0:
            num2[i] = 0
        else:
            num2[i] = num[i][1] - num2[i + 1]
            sum_val += ((num2[i] + num2[i + 1]) * (num[i][1] + 1)) // 2

for i in range(idx+1,len(num2)):
    if num[i][0] == "<":
        num2[i] = num[i - 1][1] + num2[i - 1]
        sum_val += ((num2[i] + num2[i - 1]) * (num[i][1] + 1)) // 2
    else:
        if i == len(num2) - 1:
            num2[i] = 0
        else:
            num2[i] = num[i - 1][1] - num2[i - 1]
            sum_val += ((num2[i] + num2[i - 1]) * (num[i][1] + 1)) // 2
print(num2)
print(sum_val)