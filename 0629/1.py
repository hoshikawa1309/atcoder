import collections
str = input()
counter = collections.Counter(str)

for val in counter.values():
    if val != 2:
        print("No")
        exit()
print("Yes")