date = []
N = int(input())
for i in range(366):
    if 0 <= i <= 30:
        date.append(['1/'+str(i + 1)])
    elif 31 <= i <= 59:
        date.append(['2/'+str(i - 30)])
    elif 60 <= i <= 90:
        date.append(['3/'+str(i - 59)])
    elif 91 <= i <= 120:
        date.append(['4/'+str(i - 90)])
    elif 121 <= i <= 151:
        date.append(['5/'+str(i - 120)])
    elif 152 <= i <= 181:
        date.append(['6/'+str(i - 151)])

    if 182 <= i <= 212:
        date.append(['7/'+str(i - 181)])
    elif 213 <= i <= 243:
        date.append(['8/'+str(i - 212)])
    elif 244 <= i <= 273:
        date.append(['9/'+str(i - 243)])
    elif 274 <= i <= 304:
        date.append(['10/'+str(i - 273)])
    elif 305 <= i <= 334:
        date.append(['11/'+str(i - 304)])
    elif 335 <= i <= 365:
        date.append(['12/'+str(i - 334)])
    if i % 7 == 0 or i % 7 == 6:
        date[i].append(True)
    else:
        date[i].append(False)
for _ in range(N):
    holiday = input()
    for i in range(366):
        if date[i][0] == holiday:
            if date[i][1]:
                now = i
                while now < 366:
                    if not date[now][1]:
                        date[now][1] = True
                        break
                    else:
                        now += 1
            else:
                date[i][1] = True
            break
ans = 0
now = 0
for day, flag in date:
    if flag:
        now += 1
    else:
        ans = max(ans, now)
        now = 0
ans = max(ans, now)
print(ans)