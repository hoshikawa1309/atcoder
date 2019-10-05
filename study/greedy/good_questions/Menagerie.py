N = int(input())
s = input()

def judgment(animal):
    #print(animal)
    for i in range(N):
        left = i-1
        right = i+1
        if i == 0:
            left = -1
        if i == N - 1:
            right = 0
        if animal[i] == "S" and animal[left] != animal[right] and s[i] == "o":
            return False
        elif animal[i] == "S" and animal[left] == animal[right] and s[i] == "x":
            return False
        elif animal[i] == "W" and animal[left] == animal[right] and s[i] == "o":
            return False
        elif animal[i] == "W" and animal[left] != animal[right] and s[i] == "x":
            return False
    return True

def set_animal(animal1 , animal2):
    animal_round = [animal1,animal2]
    for i in range(2,N):
        if animal_round[i-2] == "S" and animal_round[i-1] == "S":
            if s[i-1] == "o":
                animal_round.append("S")
            elif s[i-1] == "x":
                animal_round.append("W")
        elif animal_round[i-2] == "S" and animal_round[i-1] == "W":
            if s[i-1] == "o":
                animal_round.append("W")
            elif s[i-1] == "x":
                animal_round.append("S")
        elif animal_round[i-2] == "W" and animal_round[i-1] == "S":
            if s[i-1] == "o":
                animal_round.append("W")
            elif s[i-1] == "x":
                animal_round.append("S")
        elif animal_round[i-2] == "W" and animal_round[i-1] == "W":
            if s[i-1] == "o":
                animal_round.append("S")
            elif s[i-1] == "x":
                animal_round.append("W")
    return animal_round


list = [["S","S"],["W","S"],["S","W"],["W","W"]]
for e in list:
    animal_round = set_animal(e[0],e[1])
    flag = judgment(animal_round)
    #print(animal_round)
    if flag:
        break

if flag:
    print("".join(animal_round))
else:
    print(-1)
