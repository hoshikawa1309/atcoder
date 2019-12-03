N = int(input())
A = list(map(int,input().split()))
A.insert(0, 0)
A.append(0)
distance = []
sum_val = 0
for i in range(1,len(A)):
    d = abs(A[i] - A[i - 1])
    sum_val += d
    distance.append(d)
banish_list = []
now_direct = "no"
for next in range(1,len(A)):

    if A[next - 1] < A[next]:
        next_direct = "right"
    elif A[next - 1] > A[next]:
        next_direct = "left"
    else:
        next_direct = "no"
    if now_direct != next_direct and (next_direct != "no" and now_direct != "no"):
        d = min(distance[next - 1] , distance[next - 2])
    else:
        d = 0
    banish_list.append(d)
    now_direct = next_direct
banish_list.pop(0)
for b in banish_list:
    print(sum_val - b * 2)

