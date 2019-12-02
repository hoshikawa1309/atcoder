a , b = map(int,input().split())
diff = b - a
east = ((1 + diff) * diff) // 2
print(east - b)