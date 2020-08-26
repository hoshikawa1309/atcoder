a, b = map(int, input().split())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))
pins = ['x'] * 10
for p in P:
    pins[p] = '.'
for q in Q:
    pins[q] = 'o'

print(*pins[7:], sep=' ', end=' ')
print(pins[0])
print(' ', end='')
print(*pins[4:7], sep=' ')
print('  ', end='')
print(*pins[2:4], sep=' ')
print('   ', end='')
print(pins[1])