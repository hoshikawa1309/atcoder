N = int(input())
W = input()
# words1 = [W]
# words2 = []
words = [W]
for i in range(N - 1):
    next_chr = W[-1]
    W = input()
    if i % 2 == 1:
        if W in words or W[0] != next_chr:
            print("LOSE")
            exit()
        # words1.append(W)
        words.append(W)
    else:
        if W in words or W[0] != next_chr:
            print("WIN")
            exit()
        # words2.append(W)
        words.append(W)
print("DRAW")
