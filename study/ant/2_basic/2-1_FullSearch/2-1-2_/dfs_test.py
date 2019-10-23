a = "s" + "." * 2499
b = "." * 2499 + "g"
for i in range(2500):
    if i == 0:
        print(a)
    elif i == 2499:
        print(b)
    else:
        print("." * 2500)
