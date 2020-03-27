candies = list(map(int, input().split()))
candies.sort()
if candies[2] == candies[0] + candies[1]:
    print("Yes")
else:
    print("No")
