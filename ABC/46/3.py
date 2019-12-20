import math
N = int(input())
T = []
A = []
for _ in range(N):
    t , a =map(int,input().split())
    T.append(t)
    A.append(a)
sum_val = T[0] + A[0]
now_t , now_a = T[0] , A[0]
print(now_t , now_a)
for next in range(1 , N):
    # 割合が同じ時はcontinue
    if T[next] == A[next] == 1:
        continue
    # どちらも割合の方が大きい時は割合に更新
    elif T[next] >= now_t and A[next] >= now_a:
        now_t ,now_a = T[next] , A[next]

    # 片方だけ小さい時は小さい方を基準に値を更新
    elif T[next] >= now_t and A[next] < now_a:
        mul = math.ceil(now_a / A[next])
        now_t = mul * T[next]
        now_a = mul * A[next]
    elif T[next] < now_t and A[next] >= now_a:
        mul = math.ceil(now_t / T[next])
        now_t = mul * T[next]
        now_a = mul * A[next]
    # どちらの小さい時は現在大きい方を基準に更新
    else:
        add = 0
        if now_t > now_a:
            if now_t % T[next] != 0:
                add = T[next] - (now_t % T[next])
            now_t += add
            now_a = (now_t // T[next]) * A[next]
        else:
            if now_a % A[next] != 0:
                add = A[next] - (now_a % A[next])
            now_a += add
            now_t = (now_a // A[next]) * T[next]
    print(now_t , now_a)
print(now_t + now_a)