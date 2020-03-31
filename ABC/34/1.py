N, A, B, C, D = map(int, input().split())
S = list(input())

B_range = S[B - 2 : D + 1]
# print(B_range)

for i in range(len(B_range) - 1):
    if B_range[i] == B_range[i + 1] == "#":
        print("No")
        exit()

is_three = False
for i in range(len(B_range) - 2):
    if B_range[i] == B_range[i + 1] == B_range[i + 2] == ".":
        is_three = True
        break

if S[-2] == '.' and N == D:
    is_three = True

for i in range(len(S) - 1):
    if S[i] == S[i + 1] == "#":
        print("No")
        exit()
if is_three:
    print("Yes")
else:
    print("No")