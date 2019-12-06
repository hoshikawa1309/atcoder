S = list(input())
S.sort()
print("Yes" if "".join(S) == "abc" else "No")