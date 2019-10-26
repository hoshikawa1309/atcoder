import itertools
n = int(input())
k = int(input())
card = [input() for _ in range(n)]
exist = []
for num in itertools.permutations(card , k):
    nu = "".join(num)
    if not nu in exist:
        exist.append(nu)
print(len(exist))