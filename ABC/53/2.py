s = input()
for i in range(len(s)):
    if s[i] == 'A':
        A_idx = i
        break
for i in range(len(s)):
    if s[i] == 'Z':
        Z_idx = i
print(Z_idx - A_idx + 1)