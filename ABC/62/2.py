H , W = map(int,input().split())
a = list(input() for _ in range(H))
print("#" * (W + 2))
for h in a:
    print("#" , end = "")
    print(h,end = "")
    print("#")
print("#" * (W + 2))