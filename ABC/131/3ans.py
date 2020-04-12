A , B , C , D = map(int, input().split())
#最大公約数
def gcd(x , y):
    if y == 0:
        return x
    else:
        return gcd(y , x % y)

def anscount(num,C,D,cdlcm):
    sum_num = int(num / C) + int(num / D)
    ans =  sum_num - int(num / cdlcm)
    return ans

if C > D:
    cdgcd = gcd(C,D)
else:
    cdgcd = gcd(D,C)

cdlcm = int(C * D / cdgcd)

b_ans = anscount(B,C,D,cdlcm)
a_ans = anscount(A - 1,C,D,cdlcm)

ans = B - A + 1 - (b_ans - a_ans)
#print('cdgcd : ',cdgcd)
#print('cdlcm : ',cdlcm)
#print('b_ans : ', b_ans)
#print('a_ans : ', a_ans)
print(ans)
