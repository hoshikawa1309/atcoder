W, A, B = map(int, input().split())
if A <= B <= A + W or A <= B + W <= A + W or B <= A <= B + W or B <= A + W <= B + W:
    print('0')
    exit()
right_dis = max(0, abs(B - A + W))
left_dis = max(0, abs(A - B + W))
print(min(right_dis, left_dis))