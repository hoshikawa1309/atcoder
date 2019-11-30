S = list(input())
cnt = 0

for i in range(0, len(S)):
    if i == 0:
        if S[i] != "A":
            print("WA")
            exit()
    elif 2 <= i <= len(S) - 2:
        if S[i] == "C":
            cnt += 1
    if S[i].isupper() and S[i] != "C" and i != 0:
        print("WA")
        exit()

if cnt == 1:
    print("AC")
else:
    print("WA")