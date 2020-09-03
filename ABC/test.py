# setの集合演算はそんなに早くない
import time
import random
start = time.time()
s = set([int(i) for i in range(1000000)])
t = set([int(i) for i in range(0, 1000000, 2)])
for j in range(0, 100, 10):
    start = time.time()
    for i in range(j):
        z = s | t
    print(j, time.time() - start)