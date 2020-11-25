import datetime
y, m, d = map(int, input().split('/'))
now = datetime.datetime(year=y, month=m, day=d)
while not(y % m == 0 and (y // m) % d == 0):
    now = now + datetime.timedelta(days=1)
    y = now.year
    m = now.month
    d = now.day
print(str(y) + '/' + str(m).zfill(2) + '/' + str(d).zfill(2))

