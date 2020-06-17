s = input()
s = ''.join(sorted(s))
t = input()
t = ''.join(sorted(t, reverse=True))
if s < t:
    print('Yes')
else:
    print('No')

