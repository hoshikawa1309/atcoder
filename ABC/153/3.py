N, K = map(int,input().split())
H = list(map(int,input().split()))
H.sort(reverse=True)
if N <= K:
    print("0")
else:
    print(sum(H[K:]))