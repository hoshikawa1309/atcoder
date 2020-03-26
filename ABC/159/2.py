def is_kaibun(kaibun):
    for i in range(len(kaibun)//2):
        if kaibun[i] != kaibun[-i-1]:
            return False
    return True

S = input()
first = is_kaibun(S)
S_s = S[0:len(S) // 2]
second = is_kaibun(S_s)
S_t = S[len(S) // 2 + 1:len(S)]
third = is_kaibun(S_t)
if first and second and third:
    print("Yes")
else:
    print("No")