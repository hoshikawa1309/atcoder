import sys
input = sys.stdin.readline
N = int(input())
a = []
b = []
c = []
for _ in range(N):
    a_val , b_val , c_val = map(int , input().split())
    a.append(a_val)
    b.append(b_val)
    c.append(c_val)

for i in range(N - 2, -1, -1):
    a[i] += max(b[i + 1], c[i + 1])
    b[i] += max(a[i + 1], c[i + 1])
    c[i] += max(a[i + 1], b[i + 1])
print(max(a[0],b[0],c[0]))




