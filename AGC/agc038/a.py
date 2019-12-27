H , W , A , B = map(int,input().split())
before = 1
after = 0
for i in range(H):
    ans_row = []
    if i == B:
        before = 0
        after = 1
    for j in range(W):
        if A <= j:
            ans_row.append(before)
        else:
            ans_row.append(after)
    print(*ans_row , sep = "")