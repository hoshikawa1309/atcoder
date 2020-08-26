S = input()
depth = 0
if S == '{}':
    print('dict')
    exit()
for c in S:
    if c == '{':
        depth += 1
    if c == '}':
        depth -= 1
    if depth == 1 and c == ':':
        print('dict')
        exit()
print('set')