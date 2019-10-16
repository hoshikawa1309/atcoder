def dfs(s):
    if int(s) > N:
        return 0
    ret_val = 1 if all(s.count(check) for check in "357") else 0
    for c in '357':
        ret_val += dfs(s + c)
    return ret_val

N = int(input())
if N < 357:
    print("0")
    exit()


print(dfs("0"))