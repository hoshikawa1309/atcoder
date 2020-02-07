N = int(input())
num_list = [3, 5, 7]
ans = 0


def dfs(num, flag3=False, flag5=False, flag7=False):
    # 終了条件
    if num > N:
        return

    # 加算条件
    if flag3 and flag5 and flag7:
        global ans
        ans += 1

    # 探索
    dfs(num * 10 + 3, True, flag5, flag7)
    dfs(num * 10 + 5, flag3, True, flag7)
    dfs(num * 10 + 7, flag3, flag5, True)


dfs(0)
print(ans)