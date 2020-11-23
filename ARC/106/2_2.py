class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
'''
N, M = 2 * 10 ** 5, 0
A = [10 ** 9] * N
B = [10 ** 9] * N
'''
uf = UnionFind(N)
graph = [[] for _ in range(N)]
for i in range(M):
    c, d = map(int, input().split())
    uf.union(c - 1, d - 1)
    if uf.find(c - 1) < uf.find(d - 1):
        graph[uf.find(c - 1)].append(uf.find(d - 1))
    else:
        graph[uf.find(d - 1)].append(uf.find(c - 1))
print(graph)
visited = [False] * N
for i in range(N):
    if visited[i]:
        continue
    a_sum = 0
    b_sum = 0
    for node in uf.members(i):
        a_sum += A[node]
        b_sum += B[node]
        visited[i] = True
    if a_sum != b_sum:
        print('No')
        exit()
print('Yes')