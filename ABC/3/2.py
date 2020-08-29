change = set(['a', 't', 'c', 'o', 'd', 'e', 'r'])
S = input()
T = input()
for s, t in zip(S, T):
    if s == t:
        continue
    elif s == '@' and t in change:
        continue
    elif t == '@' and s in change:
        continue
    else:
        print('You will lose')
        exit()
print('You can win')