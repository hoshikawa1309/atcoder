S = input()
count = 0
start = 0
end = 1
hold_value = ""
while end <= len(S):
    if hold_value == S[start:end]:
        end += 1
    else:
        hold_value = S[start:end]
        print(hold_value)
        start = end
        end += 1
        count += 1
print(count)
