S = input()
a = int(S[:2])
b = int(S[2:])

if 1 <= a and a <= 12 and 1 <= b and b <= 12:
    print("AMBIGUOUS")
elif 1 <= a and a <= 12 and (b > 12 or b < 1):
    print("MMYY")
elif (a > 12 or a < 1) and 1 <= b and b <= 12:
    print("YYMM")
else:
    print("NA")