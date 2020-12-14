N = int(input())
s = set()
for _ in range(N):
    A = int(input())
    s.remove(A) if A in s else s.add(A)
print(len(s))