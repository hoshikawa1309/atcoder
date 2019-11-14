N = int(input())
for i in range(1,N+1):
    c = ""
    if i % 2 == 0:
        c += "a"
    if i % 3 == 0:
        c += "b"
    if i % 4 == 0:
        c += "c"
    if i % 5 == 0:
        c += "d"
    if i % 6 == 0:
        c += "e"
    if c == "":
        print(i)
    else:
        print(c)