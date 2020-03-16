N = input()[::-1]

len_N = len(N)
ans = 0
carry = False

for i in range(len_N):
    num = int(N[i])
    if num > 5:
        if carry:
            ans += 9 - num
        else:
            ans += 10 - num + 1
            carry = True
    elif num == 5:
        # 次の数が5より小さい時または、最後の桁の時
        if i == len_N - 1 or int(N[i + 1]) < 5:
            if carry:
                ans += 9 - num
            else:
                ans += 5
            carry = False
        else:
            if carry:
                ans += 9 - num
            else:
                ans += 10 - num + 1
                carry = True
    else:
        ans += num
        carry = False

print(ans)