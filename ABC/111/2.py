N = list(input())
if N[0] == N[1] == N[2]:
    print("".join(N))
else:
    num_N = int("".join(N))
    if num_N < int(N[0] * 3):
        print(N[0] * 3)
    else:
        for _ in range(3):
            print(int(N[0]) + 1,end = "")