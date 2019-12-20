S = list(input())
#keyboard = ["Do","Re","Mi","Fa","So","Ra","Si"]
keyboard = ["So","Fa","Mi","Re","Do","Si","Ra"]
for i in range(len(S)):
    if "".join(S[i:i + 5]) == "BWBWB":
        end = i
        break
print(end)
cnt = 0
for i in range(end):
    if S[i] == "W":
        cnt += 1
print(cnt)
print(keyboard[cnt % 7])