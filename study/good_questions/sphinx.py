'''
N , M = map(int , input().split())

def prime_check(n):
    if n == 1:
        return False
    for i in range(2 , int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

man = 0
oldman = 0
child = 0
while not prime_check(M):
    M -= 4
    man += 1

while M > 2:
    M -= 3
    oldman += 1
print("man",man)
print("oldman",oldman)
print("child",child)
if M == 2:
    child = 1
    print("{} {} {}".format(man , oldman,child))
else:
    print("-1 -1 -1")

N , M = map(int , input().split())
flag = False
for man_head in range(N):
    for old_head in range(2):
        for child_head in range(N):
            if man_head + old_head + child_head == N and man_head * 2 + old_head * 3 + child_head * 4 == M:
                #print("find")
                #print("man",man_head)
                #print("oldman",old_head)
                #print("child",child_head)
                flag = True
                break
        if flag:
            break
    if flag:
        break
if flag:
    print("{} {} {}".format(man_head , old_head,child_head))
else:
    print("-1 -1 -1")
'''

N , M = map(int, input().split())
for baby in range(N + 1):
    adult = baby + 3 * N - M
    elderly = -2 * N -2 * baby + M
    if baby + adult + elderly == N and 4 * baby + 3 * elderly + 2*adult == M and adult >= 0 and elderly >= 0 and baby >= 0:
        print("{} {} {}".format(adult,elderly,baby))
        exit(0)
print("-1 -1 -1")
