def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm(x, y):
    return (x * y) // gcd(x, y)

A, B, C, D = map(int, input().split())
cnt = B - A + 1
all_range = B // C + B // D - B // lcm(C , D)
sub_end = A - 1
sub_range = sub_end // C + sub_end // D - sub_end // lcm(C , D)
print(cnt - (all_range - sub_range))