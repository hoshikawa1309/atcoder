N , K = map(int , input().split())
A = list(map(int , input().split()))
S = []
for _ in range(N):
    S.append(input())
if K == len(S):
    print("")
    exit(0)

for i in range(len(S)):
    count = 0
    search_str = S[i][0]
    for value in S:
        if value[0] == search_str:
            count += 1
            if count == len(A):
                break
print(search_str)
