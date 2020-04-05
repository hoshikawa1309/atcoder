S = input()
Flags = [False] * 4
for s in S:
    if "N" == s:
        Flags[0] =True
    elif "S" == s:
        Flags[1] =True
    elif "W" == s:
        Flags[2] =True
    elif "E" == s:
        Flags[3] =True

if all(Flags) or (Flags[0] and Flags[1] and not Flags[2] and not Flags[3]) or \
        (Flags[2] and Flags[3] and not Flags[0] and not Flags[1]):
    print("Yes")
else:
    print("No")