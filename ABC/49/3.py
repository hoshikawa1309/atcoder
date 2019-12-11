S = list(input())
#S = list("dream" * 20000)
string = [list("dream") ,  list("dreamer") , list("erase") ,list("eraser")]
for i in range(4):
    string[i] = string[i][::-1]
#print(string)
S = S[::-1]
#print(S[0:5])
idx = 0
#print(S[idx:5])
while idx != len(S):
    if S[idx:idx + 5] == string[0]:
        idx += 5
    elif S[idx:idx + 7] == string[1]:
        idx += 7
    elif S[idx:idx + 5] == string[2]:
        idx += 5
    elif S[idx:idx + 6] == string[3]:
        idx += 6
    else:
        print("NO")
        exit()
print("YES")