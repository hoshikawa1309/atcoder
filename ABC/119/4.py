import bisect
A, B, Q = map(int,input().split())
shrine = tuple(int(input()) for _ in range(A))
temple = tuple(int(input()) for _ in range(B))

def dictance(place, start):
    idx = bisect.bisect_left(place, start)
    distance_list = []
    now = []
    
    # 先にplaceを回るパターン
    if idx == 0:
        distance_list.append(place[0] - start)
        now.append(place[0])

    elif idx == len(place):
        distance_list.append(start - place[-1])
        now.append(place[-1])
    else:
        distance_list.append(place[idx] - start)
        distance_list.append(start - place[idx - 1])
        now.append(place[idx])
        now.append(place[idx - 1])
    return distance_list, now


def distace2(place, start, d_list):
    distance_list2 = []
    for s, d in zip(start, d_list):
        idx = bisect.bisect_left(place, s)
        if idx == 0:
            distance_list2.append(place[0] - s + d)
        elif idx == len(place):
            distance_list2.append(s - place[-1] + d)
        else:
            distance_list2.append(place[idx] - s + d)
            distance_list2.append(s - place[idx - 1] + d)
    return distance_list2


for _ in range(Q):
    s = int(input())
    # idx = bisect.bisect_left(shrine, start)
    # ans = float('inf')
    # 先にshrineを回るパターン
    dist_list, now_list = dictance(shrine, s)
    dist2_list = distace2(temple, now_list, dist_list)
    tmp_ans = min(dist2_list)

    # 先にtempleを回るパターン
    dist_list, now_list = dictance(temple, s)
    dist2_list = distace2(shrine, now_list, dist_list)
    ans = min(dist2_list)
    print(min(tmp_ans, ans))

