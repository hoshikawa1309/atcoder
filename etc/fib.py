
def fib(n):
    if n <= 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

def memo_fib(n):
    memo = [0] * (n)
    memo[0] = 1
    memo[1] = 1
    def fib(n):
        if memo[n] != 0:
            return memo[n]
        else:
            memo[n] = fib(n - 1) + fib(n - 2)
            return memo[n]
    return fib(n)
if __name__ == "__main__":
    print(fib(40))
    print(memo_fib(40))
