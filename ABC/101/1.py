S = list(input())
num = 0
for c in S:
    if c == "+":
        num += 1
    else:
        num -= 1
print(num)