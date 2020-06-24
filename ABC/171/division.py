N = int(input())
ans = ''
for i in range(1, 99):
    if N <= 26 ** i:
        N -= 1
        for j in range(i):
            ans += chr(ord('a') + N % 26)
            N //= 26
        break
    else:
        N -= 26 ** i
print(ans[::-1])