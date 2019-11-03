N = int(input())
red = [list(map(int, input().split())) for _ in range(N) ]
blue = [list(map(int, input().split())) for _ in range(N) ]

red.sort(key = lambda x: -x[1])
red.sort(key = lambda x: -x[0])
blue.sort(key = lambda x: -x[1])
blue.sort(key = lambda x: -x[0])

ans = 0
for i in red:
    for j in blue:
        if i[0] < j[0] and i[1] < j[1]:
            red.remove(i)
            blue.remove(j)
            ans += 1
print(ans)
'''

6
0 0
7 1
7 3
2 2
4 83
2 0
3 1
1 3
4 2
0 4
5 5
1 6
8 5
6 9
5 4
9 1
3 7
5 6

'''

