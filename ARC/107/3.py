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


N, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
MOD = 998244353

A_T = []
for i in range(N):
    x = []
    for j in range(N):
        x.append(A[j][i])
    A_T.append(x)
# print(A_T)
# print(A)
row_uf = UnionFind(N)
column_uf = UnionFind(N)
for i in range(N - 1):
    row1 = A[i]
    for j in range(i + 1, N):
        row2 = A[j]
        if all([val1 + val2 <= K for val1, val2 in zip(row1, row2)]):
            row_uf.union(i, j)
# print(row_uf.all_group_members())

for i in range(N - 1):
    column1 = A_T[i]
    for j in range(i + 1, N):
        column2 = A_T[j]
        if all([val1 + val2 <= K for val1, val2 in zip(column1, column2)]):
            column_uf.union(i, j)
# print(column_uf.all_group_members())
row_cnt = 1
for root, member in row_uf.all_group_members().items():
    for i in range(len(member), 0, -1):
        row_cnt *= i
        row_cnt %= MOD

column_cnt = 1
for root, member in column_uf.all_group_members().items():
    for i in range(len(member), 0, -1):
        column_cnt *= i
        column_cnt %= MOD
print((row_cnt * column_cnt) % MOD)