N = int(input())
for cake in range(N // 4 + 1):
    for donut in range(N // 7 + 1):
        if cake * 4 + donut * 7 == N:
            print("Yes")
            exit()
print("No")