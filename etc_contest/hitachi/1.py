S = input()
hitachi = ["h", 'i']
init = 0
for i in range(len(S)):
    if not hitachi[init] == S[i]:
        print("No")
        exit()
    init = 1 - init

if init:
    print("No")
else:
    print("Yes")