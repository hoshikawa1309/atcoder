def solve():
    def gcd(x,y):
        while y != 0:
            x , y = y , x % y
        return x

    A,B,C,D = map(int ,input().split())
    A -= 1
    gcd_val = gcd(C , D)
    lcm_val = C * D // gcd_val
    ReduceFromB = B - (B // C + B // D - B // lcm_val)
    ReduceFromA = A - (A // C + A // D - A // lcm_val)
    print(ReduceFromB - ReduceFromA)

solve()