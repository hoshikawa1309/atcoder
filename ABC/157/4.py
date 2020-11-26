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


N, M, K = map(int, input().split())
uf = UnionFind(N)
direct = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    uf.union(a - 1, b - 1)
    direct[a - 1].append(b - 1)
    direct[b - 1].append(a - 1)
blocks = [[] for _ in range(N)]
for _ in range(K):
    c, d = map(int, input().split())
    blocks[c - 1].append(d - 1)
    blocks[d - 1].append(c - 1)

for i in range(N):
    num = uf.size(i) - len(direct[i]) - 1
    for block in blocks[i]:
        if uf.same(block, i):
            num -= 1
    print(num, end=' ')
print()