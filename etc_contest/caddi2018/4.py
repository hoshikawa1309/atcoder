N = int(input())
print('second' if all([int(input()) % 2 == 0 for _ in range(N)]) else 'first')
