from collections import deque
N = int(input())
nums = ['3', '5', '7']
now = ''
q = deque(nums)
ans = 0
flag = True
while flag:
    n = q.popleft()
    for num in nums:
        tmp = n
        tmp += num
        if int(tmp) > N:
            flag = False
            break
        if '3' in tmp and '5' in tmp and '7' in tmp:
            ans += 1
        q.append(tmp)

print(ans)