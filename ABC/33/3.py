S = list(input())
numList = list(map(lambda x: int(x) , S[::2]))
operandList = S[1::2]
print(numList)
print(operandList)
ans = 0
zeroFlag = False
mul_List = []
work = []
for i in range(len(operandList)):
    work.append(numList[i])
    if operandList[i] == "+":
        mul_List.append(sorted(work))
        work = []
work.append(numList[-1])
mul_List.append(work)
print(mul_List)
for val in mul_List:
    if val[0] != 0:
        ans += 1
print(ans)