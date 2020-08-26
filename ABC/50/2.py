question_num = int(input())
Time = list(map(int, input().split()))
drink_num = int(input())
spent_time = sum(Time)
drink =[]
for _ in range(drink_num):
    p, x = map(int, input().split())
    print(spent_time - (Time[p - 1] - x))
