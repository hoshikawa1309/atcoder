N = int(input())
B = list(map(int,input().split()))
ans = []
while len(ans) < N:
    for i in range(len(B) - 1, -1, -1):
        num = i + 1
        if num == B[i]:
            B.pop(i)
            ans.append(num)
            break
        if i == 0:
            print(-1)
            exit()
ans = ans[::-1]
print(*ans, sep='\n')