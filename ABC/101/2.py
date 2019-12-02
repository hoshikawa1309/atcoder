N = input()
num = 0
for c in N:
    num += int(c)
num = int(N) / num
if num.is_integer():
    print("Yes")
else:
    print("No")
