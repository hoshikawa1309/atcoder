from collections import Counter
n, c = map(int, input().split())
A = [int(input()) for _ in range(n)]
odd_counter = Counter(A[1:: 2])
even_counter = Counter(A[::2])
odd_items = list(odd_counter.values())
odd_items.sort()
even_items = list(even_counter.values())
even_items.sort()

if len(set(A)) == 1:
    print(n // 2 * c)
    exit()
ans = 0
odd_max_set = set()
even_max_set = set()
for key, val in odd_counter.items():
    if odd_items[-1] == val:
        odd_max_set.add(key)
for key, val in even_counter.items():
    if even_items[-1] == val:
        even_max_set.add(key)
if odd_max_set & even_max_set:

    if len(odd_counter.keys()) == 1:
        ans = (sum(even_counter.values()) - even_items[-2]) * c
    elif len(even_counter.keys()) == 1:
        ans = (sum(odd_counter.values()) - odd_items[-2]) * c
    else:

        ans = min((sum(odd_counter.values()) - odd_counter[max(odd_counter, key=odd_counter.get)] + sum(even_counter.values()) - even_items[-2]) * c,
                  (sum(even_counter.values()) - even_counter[max(odd_counter, key=odd_counter.get)] + sum(odd_counter.values()) - odd_items[-2]) * c)

else:
    ans = (sum(odd_counter.values()) - odd_counter[max(odd_counter, key=odd_counter.get)]
           + sum(even_counter.values()) - even_counter[max(even_counter, key=even_counter.get)]) * c
print(ans)