A ,B = map(int,input().split())
S = input()
if S[:A].isdecimal() and S[A] == "-" and S[A + 1: A  + B + 2].isdecimal():
    print("Yes")
else:
    print("No")
