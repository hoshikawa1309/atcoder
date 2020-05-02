def guumojiretu(s):
    num = len(S)
    if S[:num // 2] == S[num//2:]:
        return True
    return False
S = input()
S = S[:-1]
while True:
    if guumojiretu(S):
        break
    S = S[:-1]
print(len(S))
