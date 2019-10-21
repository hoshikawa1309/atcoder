'''
str1 = list(input())
str2 = list(input())
ans = []
for i in range(len(str1)):
    ans.extend(str1[i])
    if len(str2) != len(str1) and i == len(str1) - 1:
        break
    ans.extend(str2[i])
print("".join(ans))
'''

str1 = input()
str2 = input() + ''
for x,y in zip(str1,str2):
    print(x+y,end = '')
