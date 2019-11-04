from itertools import groupby
ans = premax = 0
for k, g in groupby(input()):
    for c, _ in enumerate(g, 1):
      ans += c
    if k == '>':
        ans -= min(c, premax)
    premax = c
print(ans)