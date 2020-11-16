N = int(input())
right_idx = 0
left_idx = N - 1
print(right_idx)
right_gender = input()
if right_gender == 'Vacant':
    exit()
print(left_idx)
left_gender = input()
if left_gender == 'Vacant':
    exit()
while True:
    middle_idx = (left_idx + right_idx) // 2
    print(middle_idx)
    middle_gender = input()
    if middle_gender == 'Vacant':
        exit()
    if (middle_idx - right_idx) % 2 == 1 and middle_gender != right_gender or\
            (middle_idx - right_idx) % 2 == 0 and middle_gender == right_gender:
        right_idx = middle_idx
        right_gender = middle_gender
    else:
        left_idx = middle_idx
        left_gender = middle_gender