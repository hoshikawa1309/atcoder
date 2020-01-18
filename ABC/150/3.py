import itertools
N = int(input())
P = list(map(int,input().split()))
Q = list(map(int,input().split()))
lst = [i for i in range(1 , N + 1)]
comp = []
for i in itertools.permutations(lst):
    comp.append(list(i))
comp.sort()
print(abs(comp.index(P) - comp.index(Q)))
