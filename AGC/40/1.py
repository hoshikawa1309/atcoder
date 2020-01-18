S = list(input())
numList = [0] * (len(S) + 1)
for i in range(len(S)):
    if S[i] == '<':
        numList[i + 1] = numList[i] + 1

for i in range(len(S) - 1 , -1 , -1):
    if S[i] == '>':
        numList[i] = max(numList[i + 1] + 1 ,numList[i])
print(sum(numList))