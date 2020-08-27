l = []
a = 'AKIHABARA'


def rec(s, i):
    if i == len(a):
        l.append(s)
        return
    if a[i] == 'A':
        rec(s, i + 1)
    rec(s + a[i], i + 1)


rec('', 0)
print("YES" if input() in l else "NO")
print(l)