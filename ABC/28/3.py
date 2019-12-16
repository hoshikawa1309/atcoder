import itertools
a = list(map(int,input().split()))
cmb_list = list(itertools.combinations(a , 3))
sum_list = []
for val in cmb_list:
    sum_list.append(sum(val))
sum_list.sort(reverse=True)
print(sum_list[2])