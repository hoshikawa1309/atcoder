
N , K , Q = map(int , input().split())
point = [K] * N
for _ in range(Q):
    answer = int(input())
    point[answer - 1] += 1
point = list(map(lambda x : x - Q , point))
for i in range(N):
    if point[i] > 0:
        print("Yes")
    else:
        print("No")
