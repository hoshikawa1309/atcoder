
def main():
    import sys
    sys.setrecursionlimit(4100000)
    H , W = map(int,input().split())
    town = [input() for _ in range(H)]
    for row in range(H):
        for column in range(W):
            if town[row][column] == "s":
                start_column , start_row = column , row
            if town[row][column] == "g":
                goal_column , goal_row = column , row
    visit_possible = [[False for _ in range(W)] for _ in range(H)]
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
    def dfs(t,r , c):
        if 0 > c or c >= W or 0 > r or r >= H or t[r][c] == "#":
            return
        if visit_possible[r][c]:
            return
        visit_possible[r][c] = True
        for i in range(4):
            dfs(t,r + dx[i],c + dy[i])
    dfs(town,start_row, start_column)
    print("Yes" if visit_possible[goal_row][goal_column] else "No")
main()
'''
4 5
s####
....#
#####
#...g
'''