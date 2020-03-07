N, A, B = map(int,input().split())
target = N % (A + B)
div_num = N // (A + B)
print(div_num * A + min(target, A))