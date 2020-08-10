N = int(input())
A = list(map(int, input().split()))
if sum(A) % N != 0:
    print('-1')
    exit()
if len(list(set(A))) == 1:
    print('0')
    exit()

need_one_island = sum(A) // N
island_cnt = 1
people = A[0]
ans = 0
for i in range(1, N):
    if people == need_one_island * island_cnt:
        island_cnt = 1
        people = A[i]
    else:
        ans += 1
        island_cnt += 1
        people += A[i]
print(ans)

