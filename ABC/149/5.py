import copy
N , M = map(int,input().split())
A = list(map(int,input().split()))
A.sort(reverse=True)
A_mirror = copy.deepcopy(A)
print(A)
print(A_mirror)
idx1 = 0
idx2 = 0
ans = 0
base = 1
is_break = False

while M > 0:
    if idx1 == idx2:
        ans += 2 * A[idx1]
        idx2 += 1
        M -= 1
        base += 1
    elif A[idx1] + A[idx2] > 2 * A[base] and idx2 < N:
        ans += A[idx1] + A[idx2]
        M -= 1
        if M == 0:
            break
        ans += A[idx1] + A[idx2]
        M -= 1
        if M == 0:
            break
        idx2 += 1
    else:
        idx1 = idx2 = base

    #print(ans)

print(ans)
