def prime_judge(x):
    for i in range(2, int(x ** (1 / 2)) + 1):
        if x % i == 0:
            return False
    return True


X = int(input())
while not prime_judge(X):
    X += 1
print(X)