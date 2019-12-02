'''
N = int(input())
S = list(input())
i = 1
cnt = 0
while i < len(S):
    if S[i-1] == S[i]:
        cnt += 1
    else:
        cnt = 0
    if cnt >= 4:
        S.pop(i)
    else:
        i += 1
#print(S)
pin = [0] * 1000
for i in range(len(S) - 2):
    for j in range(i + 1 , len(S) - 1):
        for k in range(j + 1 , len(S)):
            now = S[i] + S[j] + S[k]
            pin[int(now)] = 1
            if all(pin):
                print(sum(pin))
                exit()
print(sum(pin))

'''