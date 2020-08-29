keys = ['Fa', 'Mi', 'Re', 'Re', 'Do', 'Do', 'Si',  'La', 'La', 'So', 'So', 'Fa']
S = input()
for i in range(13):
    if S[i: i + 7] == 'WBWBWBW':
        print(keys[i % len(keys)])
        exit()