N =int(input())
S = list(input())
ans = []
for val in S:
    c = ord(val) + N
    if c > 90:
        c -= 26
    ans.append(chr(c))
print("".join(ans))