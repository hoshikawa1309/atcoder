N = int(input())
red = []
blue = []
for _ in range(N):
    a , b = map(int,input().split())
    red.append([(a ** 2 + b ** 2) ** (1 / 2),a , b ])
    #red.append([a, b])
for _ in range(N):
    a, b = map(int, input().split())
    blue.append([(a ** 2 + b ** 2) ** (1 / 2),a , b ])
    #blue.append([a, b])

red.sort(reverse=True)
#red.sort(reverse=True , key= lambda x: x[1])
blue.sort()
#blue.sort(key= lambda x: x[1])
find = []
for i in range(N):
    for j in range(N-1 , -1 ,-1):
        if red[i][1] < blue[j][1] and red[i][2] < blue[j][2] and not blue[j] in find:
        #if red[i][1] < blue[j][1] and red[i][0] < blue[j][0] and not blue[j] in find:
            find.append(blue[j])
            break
print(len(find))

