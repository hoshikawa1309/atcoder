S = input()
t = int(input())
values = set()
for i in range(len(S) - t + 1):
    # print(S[i:i + t])
    values.add(S[i: i + t])
print(len(values))