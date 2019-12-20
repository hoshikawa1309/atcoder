sx , sy ,tx ,ty = map(int,input().split())
for _ in range(ty - sy):
    print("U",end = "")
for _ in range(tx - sx):
    print("R",end = "")
for _ in range(ty - sy):
    print("D",end = "")
for _ in range(tx - sx):
    print("L",end = "")

print("L" , end = "")
for _ in range(ty - sy + 1):
    print("U",end = "")
for _ in range(tx - sx + 1):
    print("R",end = "")
print("D" , end = "")
print("R" , end = "")
for _ in range(ty - sy + 1):
    print("D",end = "")
for _ in range(tx - sx + 1):
    print("L",end = "")
print("U")
print("UURRURRDDDLLDLLULUUURRURRDDDLLDL")

