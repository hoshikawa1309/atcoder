S = list(input())
lenS = len(S)
ans = 0
for i in range(2 ** (lenS - 1)):
    formula = []
    for j in range(lenS):
        formula.append(S[j])
        if i >> j & 1:
            formula.append("+")
    ans += eval("".join(formula))
print(ans)