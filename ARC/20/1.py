ant, bug = map(int,input().split())
ant = abs(ant)
bug = abs(bug)
if ant == bug:
    print('Draw')
elif ant < bug:
    print('Ant')
else:
    print('Bug')