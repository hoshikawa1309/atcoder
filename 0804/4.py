'''
S = input()
right_count = 0
left_count = 0
right_index = 0
left_index = 0
counter = 0
ans = [0] * len(S)
for i in range(len(S) - 1):
    counter += 1
    if S[i] == 'R' and S[i + 1] == 'L':
        right_index = i + 1
        left_index = i
        start = i
    if S[i] == "L" and S[i + 1] == "R" or i == len(S) - 2:
        if i == len(S) - 2:
            counter += 1
        odd_count = counter // 2
        even_count = counter - odd_count
        if start % 2 == 1:
            ans[left_index] = odd_count
            ans[right_index] = even_count
        else:
            ans[left_index] = even_count
            ans[right_index] = odd_count
        counter = 0

for i in range(len(S)):
    print(ans[i] , end = " ")

'''
S = input()
S = S + "R"
odd_count = 0
even_count = 0
ans = [0] * len(S)
for i in range(len(S) - 1):
    if i % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
    if S[i] == 'R' and S[i + 1] == 'L':
        right_index = i + 1
        left_index = i
        start = i
    if S[i] == "L" and S[i + 1] == "R":
        if start % 2 == 1:
            ans[left_index] = odd_count
            ans[right_index] = even_count
        else:
            ans[left_index] = even_count
            ans[right_index] = odd_count
        odd_count = 0
        even_count = 0
for i in range(len(S) - 1):
    print(ans[i] , end = " ")