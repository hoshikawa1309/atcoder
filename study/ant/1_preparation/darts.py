'''
def main():
    from functools import lru_cache
    N , M = map(int,input().split())
    points = [int(input()) for _ in range(N)]
    #print(points)

    @lru_cache(maxsize = 2 * 10 ** 8)
    def solve(idx, margin , darts_cnt):
        if idx == -1 or darts_cnt == 4:
            ret_val = 0
        elif margin < points[idx]:
            ret_val = solve(idx - 1, margin, darts_cnt)
        else:
            point = points[idx]
            ret_val = max(solve(idx - 1, margin , darts_cnt), solve(idx , margin - point , darts_cnt + 1) + point)
        # print(idx , margin , ret_val)
        return ret_val
    print(solve(N - 1, M, 0))
main()
'''

from itertools import product
import bisect

n, m = map(int, input().split())
p = [int(input()) for i in range(n)]
p.append(0)

# productを用いて直積を求める。2投分の組み合わせ（半分全列挙）を行う
se = set()
for i, j in product(p, p):
    se.add(i + j)
li = list(sorted(se))

ans = 0
# 半分全列挙を行なったリストと、そのリストのi番目の数とm - li[i]の差の中で取り得る値を考える
# それにより、1,2投分の点数　＋　（m - 1, 2投分の点数）より3 、４投分の得点を考えることができ、それを最大化する。
for i in li:
    idx = bisect.bisect_right(li, m - i)
    if i + li[idx - 1] <= m:
        ans = max(ans, i + li[idx - 1])
print(ans)