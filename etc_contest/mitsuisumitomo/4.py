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

N = int(input())
S = list(input())
S = list(map(int,S))
pin = [0,0,0]
ans = 0
for i in range(1000):
    pin[0] = i // 100
    pin[1] = (i // 10) % 10
    pin[2] = i % 10
    cnt = 0
    #print(pin)
    for j in range(N):
        if pin[cnt] == S[j]:
            cnt += 1
        if cnt == 3:
            ans += 1
            break
print(ans)

