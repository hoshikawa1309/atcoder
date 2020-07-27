S = []
Sa = input()
S.append(list(Sa.replace('a', '0').replace('b', '1').replace('c', '2')))
Sb = input()
S.append(list(Sb.replace('a', '0').replace('b', '1').replace('c', '2')))
Sc = input()
S.append(list(Sc.replace('a', '0').replace('b', '1').replace('c', '2')))

now = [0] * 3
turn = 0
len_a = len(Sa)
len_b = len(Sb)
len_c = len(Sc)

while True:
    if (now[0] == len_a and turn == 0) or (now[1] == len_b and turn == 1) or (now[2] == len_c and turn == 2):
        break
    next_turn = S[turn][now[turn]]
    now[turn] += 1
    turn = int(next_turn)

print(chr(ord('A') + turn))
