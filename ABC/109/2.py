N = int(input())
now = list(input())
already = [now]
Flag = False
for _ in range(N - 1):
    next_word = list(input())
    if next_word in already or now[-1] != next_word[0]:
        Flag = True
        break
    already.append(next_word)
    now = next_word

print("No" if Flag else "Yes")