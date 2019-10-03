s = list(input())
t = list(input())
work = s[:]
cnt = 0
ans = 0
flag = False
while cnt < len(t):
    print("t[count] ",t[cnt])
    print("work ",work)
    try:
        index = work.index(t[cnt])
        #print("index" , index)
        ans += index + 1
        cnt += 1
        work = work[index + 1:]
        #print("work",work)
        flag = False
    except ValueError:
        if flag:
            print(-1)
            exit(0)
        #print("len(work)",len(work))
        print("not find")
        ans += len(work)
        work = s[:]
        #print("work",work)
        flag = True
    print("ans ",ans)
print(ans)
