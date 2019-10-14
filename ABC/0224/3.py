N , A , B , C = map(int,input().split())
l = [int(input()) for _ in range(N)]
print(l)
def dfs( n , a, b, c):
    if n == N:
        if min(a,b,c) > 0:
            # min(a,b,c)を通る時、必ず + 10 + 10 + 10が発生している。この時、0から1本目の結合は1本目の洗濯と同義であり、
            # その時魔法力は使用しないため、-30が必要になる。
            return abs(A - a) + abs(B - b) + abs(C - c) - 30
        else:
            return 10 ** 9
    w = dfs(n + 1, a , b, c)
    x = dfs(n + 1, a + l[n], b, c) + 10
    y = dfs(n + 1, a, b + l[n], c) + 10
    z = dfs(n + 1, a, b, c + l[n]) + 10
    return min(w ,x , y , z)

print(dfs(0,0,0,0))