N , K , M = map(int,input().split())
A = list(map(int,input().split()))
target = M * N - sum(A)
if target <= K:
    if target < 0:
        print("0")
    else:
        print(target)
else:
    print("-1")