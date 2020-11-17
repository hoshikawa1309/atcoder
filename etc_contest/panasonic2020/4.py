N = int(input())
alph = [chr(ord('a') + i) for i in range(26)]
# print(alph)
for i in range(2 ** N - 2 ** (N - 1)):
    pointer = 1
    for j in range(N - 1, -1, -1):
        if i >> j & 1:
            print(alph[pointer], end='')
            pointer += 1
        else:
            print('a', end='')
    print()

