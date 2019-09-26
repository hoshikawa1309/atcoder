N = int(input())
count = []
for i in range(N):
    str = input()
    counter = 0
    while "tokyo" in str or "kyoto" in str:
        if str.find("tokyo") != -1 and str.find("kyoto") != -1:
            start = min(str.find("tokyo"),str.find("kyoto"))
        elif str.find("tokyo") == -1:
            start = str.find("kyoto")
        elif str.find("kyoto") == -1:
            start = str.find("tokyo")
        end = start + 5
        str = str[end:]
        counter += 1
    count.append(counter)
print(*count, sep = "\n")


