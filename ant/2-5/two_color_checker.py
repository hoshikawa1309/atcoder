from collections  import deque
'''
N = int(input())
graph = [[] for _ in range(N)]
for _ in range(N - 1):
    a , b , w = map(int , input().split())
    a -= 1
    b -= 1
    graph[b].append([a,w])
    graph[a].append([b,w])

#print(len(graph.pop()[0]))
#print(graph.pop())
#print(len(graph.pop()))
def dfs():
    q = deque(graph[0])
    color = [0] * N
    corrent_color = 0
    other_color = 1
    searched = [0]
    while q:
        count = len(q)
        #print(count)
        search = q.popleft()
        #print("search : ",search)
        #print("search[0] : ",search[0])
        #print(len(search))
        for i in range(count):

            if not search[0] in searched:
                searched.append(search[0])
                if search[1] % 2 == 0:
                    color[search[0]] = corrent_color
                else:
                    color[search[0]] = other_color
                #print(len(graph[search[0]]))
                #print(graph[search[0]][0])
                for i in range(len(graph[search[0]])):
                    #print("i : ",i)
                    #print(graph[search[0]][i])
                    q.append(graph[search[0]][i])
                #print(q)
        corrent_color = color[search[0]]
        other_color = 1 - corrent_color
    print(*color , sep = "\n")
dfs()
'''

N = int(input())
graph = [[] for _ in range(N)]
cost = [[] for _ in range(N)]
for _ in range(N - 1):
    a , b , w = map(int , input().split())
    a -= 1
    b -= 1
    graph[b].append(a)
    graph[a].append(b)
    cost[b].append(w % 2)
    cost[a].append(w % 2)

color = [-1] * N
color[0] = 0
q = deque()
q.append(int(0))

#print(cost[0])
#print(graph[0])
while q:
    value = q.popleft()
    #print(value)
    for to , c in zip(graph[value] , cost[value]):
        #print(to , c)
        if color[to] != -1:
            continue
        color[to] = color[value]^c
        q.append(to)
print(*color , sep = "\n")
