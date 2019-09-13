import numpy as np
S = input()
children = [1] * len(S)
for i in range(10**5):
    if i % 1000 == 0:
        print(i)
    index = i % len(S)
    if children[index] == 0:
        continue
    elif S[index] == "R":
        children[index] -= 1
        children[index + 1] += 1
    elif S[index] == "L":
        children[index] -= 1
        children[index - 1] += 1
print(children)
