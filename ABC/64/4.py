N = int(input())
S = input()
now = 0
right = 0
left = 0
add_left = 0
while now < N:
    if S[now] == '(':
        left += 1
    else:
        if left:
            left -= 1
        else:
            add_left += 1
    now += 1
for _ in range(add_left):
    print('(', end='')
print(S, end='')
for _ in range(left):
    print(')', end='')

