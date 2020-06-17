weather = ['Sunny', 'Cloudy', 'Rainy', 'Sunny']
S = input()
for i in range(3):
    if weather[i] == S:
        print(weather[i + 1])
        exit()