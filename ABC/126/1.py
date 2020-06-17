N , K = map(int ,input().split())
S = list(input())
K -= 1
#print(S[K])
#print(ord(S[K]))
#print(ord(S[K]) + 1)
S[K] = chr(ord(S[K]) + 32)
print("".join(S))