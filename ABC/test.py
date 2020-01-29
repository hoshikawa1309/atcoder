from numpy.random import *
n = 10**5
l1 = randint(1, n, n)
l2 = randint(1, n, n)


with open("./test_case.txt",mode="w") as f:
    for val in zip(l1, l2):
        # print(l1[i], l2[i])
        row = str(val)
        f.writelines("\n".join(row))