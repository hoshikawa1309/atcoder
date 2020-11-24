def solve(r1, c1, r2, c2):
    # 0手のとき
    if r1 == r2 and c1 == c2: return 0
    w1 = r1 + c1
    g1 = r1 - c1
    w2 = r2 + c2
    g2 = r2 - c2
    # 1手のとき
    if w1 == w2 or g1 == g2: return 1
    if max(abs(w1 - w2), abs(g1 - g2)) <= 3: return 1
    # 2手のとき
    if abs(w1 - w2) % 2 == 0 and abs(g1 - g2) % 2 == 0: return 2
    if abs(w1 - w2) <= 3 or abs(g1 - g2) <= 3: return 2
    if max(abs(w1 - w2), abs(g1 - g2)) <= 6: return 2
    return 3


if __name__ == '__main__':
    r1, c1 = map(int, input().split())
    r2, c2 = map(int, input().split())
    print(solve(r1, c1, r2, c2))