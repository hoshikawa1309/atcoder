A, B = map(int, input().split())
cards = [i for i in range(2, 14)] + [1]
A = cards.index(A)
B = cards.index(B)
if A > B:
    print('Alice')
elif B > A:
    print('Bob')
else:
    print('Draw')