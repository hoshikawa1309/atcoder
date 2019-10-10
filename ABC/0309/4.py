'''
def solve(x):
    work_x = x
    i = 1
    while True:
        if 2 ** i > B:
            break
        i += 1
    i -= 1
    #print(2 ** i)
    bit_list = []
    while i >= 0:
        if i == 0:
            if B % 4 >= 2:
                bit_list.append(0)
            if B % 4 < 2:
                bit_list.append(1)
        else:
            bit = work_x - 2 ** i + 1
            work_x -= 2 ** i
            bit_list.append(bit % 2)
        i -= 1
    return bit_list

A , B = map(int,input().split())
A_list = solve(A)
B_list = solve(B)
print(A_list)
print(B_list)
A_list = A_list[-1]
B_list = B_list[-1]
y = 0
ansA = 0
for i in A_list:
    ansA += i ** y
    y += 1
ansB = 0
for i in B_list:
    ansB += i ** y
    y += 1
print(ansA)
print(ansB)
print(ansA ^ ansB)
'''


def f(x):
    if x % 4 == 0:
        return x
    elif x % 4 == 1:
        return 1
    elif x % 4 == 2:
        return x + 1
    else:
        return 0


def main():
    a, b = map(int, input().split())
    A = f(a - 1)
    B = f(b)
    print(A ^ B)


if __name__ == '__main__':
    main()