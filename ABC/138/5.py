s = list(input())
t = list(input())
not_exist_flag = 0
finish_flag = False
t_index = 0

for count in range(len(s)):
    for char_num in range(len(s)):
        if t[t_index] == s[char_num]:
            if t_index == len(t) - 1:
                finish_flag = True
                break
            t_index += 1
    if finish_flag:
        break

if t_index != len(t) - 1:
    print(-1)
else:
    print(count * len(s) + char_num + 1)
