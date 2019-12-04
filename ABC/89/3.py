N = int(input())
NameList = []
CharCnt = [0] * 5
CharList = ["M","A","R","C","H"]
for _ in range(N):
    S = input()
    for i in range(5):
        if S[0] == CharList[i]:
            CharCnt[i] += 1
ans = 0
#print(CharCnt)
for i in range(3):
    for j in range(i + 1, 4):
        for k in range(j + 1, 5):
            tmp_ans = CharCnt[i] * CharCnt[j] * CharCnt[k]
            if tmp_ans != 0:
                ans += tmp_ans
if sum(CharCnt) < 3:
    print("0")
else:
    print(ans)