A, B = map(int, input().split())
ans = 0
while A % 4 != 0:
    ans ^= A
    A += 1

while B % 4 != 3:
    ans ^= B
    B -= 1
print(ans)