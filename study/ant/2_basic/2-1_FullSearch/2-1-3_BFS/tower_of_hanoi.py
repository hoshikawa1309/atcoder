def hanoi( n , frm , tmp , to):
    if n == 1:
        print(frm +" → "+to)
        return
    hanoi(n - 1 ,frm , to, tmp)
    print(frm + " → " + to)
    hanoi(n - 1,tmp,frm , to)


hanoi(4 , "A" , "B" , "C")