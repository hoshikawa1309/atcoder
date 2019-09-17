'''
N = int(input())
S = input()
ans = 0
for i in range(N // 2):
    for j in range(i + 1, N):
        str = S[i:j]
        search = S[j:]
        print(search[:i + 1])
        if str == search[:i + 1]:
            ans = len(str)
print(ans)

n = int(input())
s = input()

l1 = l2 = length = 0

while l2 + length < n:
    if s[l1: l2] in s[l2:]:
        length = l2 - l1
        l2 += 1
    else:
        l1 += 1
        l2 = l1 + length + 1

print(length)
'''

n = int(input())
s = input()

l1 = l2 = length = 0

while l2 + length < n:
    print("s[l1:l2]" , s[l1:l2])
    print("s[l2:]" , s[l2:])
    if s[l1:l2] in s[l2:]:
        length = l2 - l1
        l2 += 1
    else:
        l1 += 1
        l2 = l1 + length + 1
print(length)