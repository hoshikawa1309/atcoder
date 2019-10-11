S = list(input())
i = 0
cnt = 0
while i < len(S):
    #print(S)
    if "".join(S[i:i+2]) == "01" or "".join(S[i : i + 2]) == "10":
        if i + 1< len(S):
            S.pop(i + 1)
        S.pop(i)
        cnt += 2
        i = max(0 , i - 1)
    else:
        i += 1
print(cnt)
