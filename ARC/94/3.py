ABC = list(map(int, input().split()))
ABC.sort(reverse=True)
max_val = ABC[0]
second_max_val = ABC[1]
ans = max_val - second_max_val
min_val = ABC[2] + ans
diff = max_val - min_val
if diff % 2 == 0:
    ans += diff // 2
else:
    ans += diff // 2 + 2
print(ans)
