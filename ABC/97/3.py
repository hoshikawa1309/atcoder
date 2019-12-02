S = list(input())
N = len(S)
K = int(input())
ans = []
for start in range(N):
    for end in range(K):
        if start + end >= N:
            break
        sentinel = min(N - 1 , start + end)
        ans.append(S[start:sentinel + 1])

i = 0
ans.sort()
answer = []
while len(answer) < K:
    if not ans[i] in answer:
        answer.append(ans[i])
    i += 1
print("".join(answer[K - 1]))