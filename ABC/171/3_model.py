# [基本方針]
# コンプロでもやった進数変換の応用問題。今回は26進数変換を基本に考える。
# 1:aではなく、0:aを対応していると考える。そのため、26で割ったあまりを考える時、0:a、1:b,..., z:25と考えることができる。
# 計算量はO(logN)
# 参考：https://www.youtube.com/watch?v=TUdZT1wIbe8&feature=youtu.be


N = int(input())
ans = ''
while N:
    # 1をaではなく、0をaに割り当てると考えるため、N-=1を行う。
    N -= 1

    # ここから下は基本的な進数変換と同じ
    alphabet = chr(ord('a') + N % 26)
    ans += alphabet
    N //= 26

# 文字列を反転させる
print(ans[::-1])
