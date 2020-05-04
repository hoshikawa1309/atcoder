S = input()
Counter = {"a": 0, "b": 0,"c": 0}
for c in S:
    Counter[c] += 1
# print(Counter)
max_val = max(Counter.values())
min_val = min(Counter.values())
if max_val - min_val <= 1:
    print("YES")
else:
    print("NO")