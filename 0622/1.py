str = input()
flag = 0
#print(type(str))
#print(len(str))
for i in range(len(str) - 1):
    if str[i] == str[i + 1]:
        flag = 1

if flag == 1:
    print("Bad")
else:
    print("Good")
