#from Collections import Counter

N = int(input())
count = 0
word = {}
def str_sort(str):
    f = lambda y: "".join(sorted(map(lambda x: x.replace(' ', '').lower(), y)))
    return f(str)
for _ in range(N):
    sorted_str = str_sort(input())
    if sorted_str not in word:
        word[sorted_str] = [0]
        word[sorted_str].append(1)
    else:
        if word[sorted_str] == 0:
            word[sorted_str][0] = 1
        else:
            word[sorted_str][0] += word[sorted_str][1]
            word[sorted_str][1] += 1
            #word[sorted_str] = word[sorted_str][0] + word[sorted_str][1]
total = sum(
    v[0] for v in word.values()
)
#print(word)
print(total)
