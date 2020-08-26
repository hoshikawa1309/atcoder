from collections import Counter
import math
N, M = map(int, input().split())
name = input()
kit = input()
name_set = set(name)
kit_set = set(kit)
if len(name_set & kit_set) != len(name_set):
    print('-1')
    exit()

name_counter = Counter(name)
kit_counter = Counter(kit)
ans = 0
for key, val in name_counter.items():
    ans = max(math.ceil(val / kit_counter[key]), ans)
print(ans)