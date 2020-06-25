import bisect
N, M = map(int, input().split())
start_to_middle = []
middle_to_end = []
for i in range(M):
    a, b = map(int, input().split())
    if a == 1:
        start_to_middle.append(b)
    elif b == N:
        middle_to_end.append(a)
if not len(start_to_middle) or not len(middle_to_end):
    print('IMPOSSIBLE')
    exit()
middle_to_end.sort()
for middle in start_to_middle:
    idx = bisect.bisect_left(middle_to_end, middle)
    if idx < len(middle_to_end) and middle_to_end[idx] == middle:
        print('POSSIBLE')
        exit()

print('IMPOSSIBLE')
