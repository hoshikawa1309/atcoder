N, K = map(int, input().split())
have_treat = [True] * N

for _ in range(K):
    _ = int(input())
    treat = list(map(int, input().split()))
    for a in treat:
        a -= 1
        have_treat[a] = False
print(sum(have_treat))