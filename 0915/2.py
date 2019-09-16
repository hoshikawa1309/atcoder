S = input()
even = S[0::2]
odd = S[1::2]

if not "L" in even and not "R" in odd:
    print("Yes")
else:
    print("No")
