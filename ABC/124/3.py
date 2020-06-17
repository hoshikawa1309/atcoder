S = list(map(int , input()))
lst0 = []
lst1 = []
for i in range(len(S)):
    lst1.append(i % 2)
    lst0.append((i + 1) % 2)
cnt0 = 0
cnt1 = 0
for i in range(len(S)):
    if S[i] != lst0[i]:
        cnt0 += 1
    if S[i] != lst1[i]:
        cnt1 += 1
print(min(cnt0,cnt1))