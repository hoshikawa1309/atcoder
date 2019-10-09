#import numpy as np
x = [input() for _ in range(5)]
ans = []
for i in range(5):
    if x[i][-1] == "0":
        ans.append(int(x[i]))
for j in range(9,0,-1):
    for i in range(5):
        if int(x[i][-1]) == j:
            if len(ans) != 4:
                for k in range(1,10):
                    if (int(x[i]) + k )% 10 == 0:
                        ans.append(int(x[i]) + k)
            else:
                ans.append(int(x[i]))

print(sum(ans))
