A = list(input())
if len(A) >= 2:
    print("".join(A[:len(A) - 1]))
elif A[0] == "a":
    print("-1")
else:
    print(chr(ord(A[0]) - 1))