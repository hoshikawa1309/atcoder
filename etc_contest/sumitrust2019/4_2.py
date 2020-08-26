N = int(input())
S = input()
pattern = [False] * 1000

for i in range(1000):
    str_i = str(i)
    str_i = str_i.zfill(3)
    now = 0
    for c in S:
        if c == str_i[now]:
            now += 1
        if now == 3:
            pattern[i] = True
            break
print(sum(pattern))