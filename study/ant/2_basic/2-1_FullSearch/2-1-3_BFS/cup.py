import sys
sys.setrecursionlimit(10**5)

def recursion(start,work,end):
    pass

n_list = []
m_list = []
a_list = []
b_list = []
c_list = []
while True:
    n , m = map(int,input().split())
    if n == m == 0:
        break
    n_list.append(n)
    m_list.append(m)
    a = list(input().split())
    a_list.append(a)
    b = list(input().split())
    b_list.append(b)
    c = list(input().split())
    c_list.append(c)

for i in range(len(n_list)):

