A , B , K = map(int,input().split())
takahashi_num = max(A - K , 0)
if takahashi_num == 0:
    aoki_num = max(B - (K - A) , 0)
else:
    aoki_num = B
print(takahashi_num , aoki_num)