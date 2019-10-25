## TLE吐いていた一番の原因はvisitedリストを作成し、そこ含まれているか否かを毎回判定していたことと考えられる
## そのため、in visitedを使うのをやめ、score配列を作成し-1で初期化することにより-1か否かで判定を行うことで
## 高速化に成功した。
def main():
    from collections import deque
    import sys
    def input():
        return sys.stdin.readline()[:-1]
    # 入力
    H , W , N = map(int,input().split())
    maze = [list(input()) for _ in range(H)]
    ob = []
    for i in range(H):
        for j in range(W):
            if maze[i][j] != "X" and maze[i][j] != ".":
                ob.append([maze[i][j],i,j])
    ob.sort()
    s_tmp = ob.pop()
    ob.insert(0,s_tmp)
    def bfs(start_y , start_x , goal_y,goal_x , m):
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        score = [[-1 for _ in range(W)] for _ in range(H)]
        q = deque()
        q.append([start_y , start_x])
        score[start_y][start_x] = 0
        while q:
            y , x = q.popleft()
            for i in range(4):
                next_y , next_x = y + dy[i] ,x + dx[i]
                if next_x < 0 or W <= next_x or next_y < 0 or H <= next_y:
                    continue
                if m[next_y][next_x] == "X" or score[next_y][next_x] != -1:
                    continue
                score[next_y][next_x] = score[y][x] + 1
                q.append([next_y,next_x])
        return score[goal_y][goal_x]

    count = 0
    for i in range(len(ob) - 1):
        count += bfs(ob[i][1],ob[i][2] , ob[i + 1][1] , ob[i + 1][2] , maze)
    print(count)
main()