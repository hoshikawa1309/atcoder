S = input()
lst = ["SUN","MON","TUE","WED","THU","FRI","SAT"]
lst = lst[::-1]
for i ,val in enumerate(lst):
    if val == S:
        print(i + 1)
        exit()