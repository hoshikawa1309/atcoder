K , S = map(int , input().split())
count = 0
for i in range(0 , K + 1):
  for j in range(0 , K + 1):
    for k in range(0 , K + 1):
      if i + j + k == S:
	      count += 1
print(count)
