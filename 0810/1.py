a , b  = map(int,input().split())
add = a + b
sub = a - b
mul = a * b
if add >= sub and add >= mul:
	max = add
elif sub >= add and sub >= mul:
  	max = sub
else:
    max = mul
print(max)
