T = int(input())
s = []
for _ in range(T):
    s.append(list(input()))

for val in s:
    ans = 0
    i = 0
    while i < len(val) - 4:
        check_s = val[i:i + 5]
        check_s = "".join(check_s)
        if check_s == "tokyo" or check_s == "kyoto":
            ans += 1
            i += 5
        else:
            i += 1
    print(ans)