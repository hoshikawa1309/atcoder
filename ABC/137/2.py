K , X = map(int , input().split())

length = K - 1

start = X - length
end = X + length

for i in range(start , end + 1):
    print(i , " " , end = '')
print()
