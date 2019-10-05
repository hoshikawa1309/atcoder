from collections import deque
def main():
    N , M = map(int , input().split())
    graph = [[] for _ in range(N)]
    for _ in range(M):
        frm , to = map(int ,input().split())
        graph[frm - 1].append([to - 1])
    #print(graph)
    dp = [0] * N
    for i in range(M):
        q = deque(graph[0])
        idx = 0
        while deque:
            value = q.popleft()
            dp[value] = dp[idx] + 1
            idx = value
            q.append(graph[value])
    print(dp)
main()