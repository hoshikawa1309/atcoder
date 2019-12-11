N = int(input())
def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            #if i != n // i:
            divisors.append(n//i)

    divisors.sort()
    return divisors
div_lst = make_divisors(N)
len_div = len(div_lst)
ans = float("inf")
for i in range(len_div):
    tmp_ans = max(len(str(div_lst[i])) , len(str(div_lst[len_div - i - 1])))
    if ans > tmp_ans:

        ans = tmp_ans
print(ans)