import math
A, B, C, D = map(int, input().split())
A -= 1
lcm = (C * D) // math.gcd(C, D)
B_sum = B - (B // C) - (B // D) + (B // lcm)
A_sum = A - (A // C) - (A // D) + (A // lcm)
print(B_sum - A_sum)