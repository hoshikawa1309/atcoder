from collections import deque
N = int(input())

def dfs(str):
    if len(str) == N:
        print(*str, sep="")
        return

    M = max(str)

    for i in range(ord(M) - ord("a") + 2):
        char = alpha[i]
        str.append(char)
        dfs(str)
        str.pop()

alpha = 'abcdefghijklmnopqrstuvwxyz'
s = deque(["a"])
dfs(s)

