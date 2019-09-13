N = int(input())

#I = [i for i in range(1,N + 1)]
#ans = int(N * (N-1) / 2) + N % 1
ans = N * (N - 1) // 2
print(ans)

'''
for i in range(1 , N + 1):
    #print(I[i])
    if i == N:
        ans += i % 1
    else:
        ans += i % (i + 1)
    #print(ans)
print(ans)
'''
