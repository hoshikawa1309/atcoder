A = int(input())
B = int(input())
C = int(input())
D = int(input())
P = int(input())

print(min(P * A, max(0 , (P - C)) * D + B))

