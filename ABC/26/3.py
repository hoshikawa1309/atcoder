N = int(input())
salary = [1] * N

B = [[] for _ in range(N)]
for i in range(1,N):
    x = int(input())
    salary[x - 1] = 0
    B[x - 1].append(i)
while not salary[0]:
    for i in range(N):
        if B[i] == []:
            continue
        work = []
        for subordinate in B[i]:
            if salary[subordinate] == 0:
                break
            work.append(salary[subordinate])
        else:
            salary[i] = max(work) + min(work) + 1
print(salary[0])

