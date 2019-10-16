N = int(input())
p = list(int(input()) for _ in range(N))
p.sort()
work = p.pop()
work = work // 2
p.append(work)
print(sum(p))