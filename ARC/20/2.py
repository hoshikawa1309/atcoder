from collections import Counter
n, c = map(int, input().split())
A = [int(input()) for _ in range(n)]
odd_counter = Counter(A[1:: 2])
even_counter = Counter(A[::2])
odd_list = []
even_list = []
for key, val in odd_counter:
    odd_list.append([key, val])
for key, val in even_counter:
    even_list.append([key, val])

ans = 0
if odd_list[0][0] != even_list[0][0]:
    ans = (len(odd_list) - odd_list[0][1]) * c + (len(even_list) - even_list[0][1]) * c
else:
    if len(odd_list) == 1:
        ans = (len(even_list) - even_list[1][0]) * c
    elif len(even_list) == 1:
        ans = (len(odd_list) - odd_list[1][0]) * c
    else:
        odd_cnt = odd_list[0][1]
        even_cnt = even_list[0][1]
        if odd_cnt >= even_cnt:
            pass


