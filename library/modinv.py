def modinv(a, m):
    b = m
    u = 1
    v = 0
    while b:
        t = a // b
        a -= t * b
        a, b = b, a
        u -= t * v
        u, v = v, u
    u %= m
    if u < 0:
        u += m
    return u

if __name__ == '__main__':
    for i in range(1, 13):
        print(str(i) + "'s inv : " + str(modinv(i, 13)))