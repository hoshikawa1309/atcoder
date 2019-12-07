S = list(input())
before = S[:len(S) // 2]
after = S[len(S) // 2:]
for i in range(len(S) // 2):
    tmp = before.pop(-1)
    after.insert(0 , tmp)
    after.pop(-1)
    after.pop(-1)
    if before == after:
        break
print(len(before) * 2)