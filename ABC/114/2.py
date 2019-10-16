S = list(input())
#print(S)
min = float("inf")
#print(min)
for i in range(len(S) - 2):
    tmp_min = abs(753 - int("".join(S[i:i + 3])))
    if tmp_min < min:
        min = tmp_min
print(min)
