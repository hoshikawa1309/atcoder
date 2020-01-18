def main():
	md=998244353
	n=int(input())
	s = input()
	r=[]
	g=[]
	b=[]
	for i in range(n*3):
		if s[i]=="R":r.append(i+1)
		elif s[i]=="G":g.append(i+1)
		else:b.append(i+1)

	u=[]
	m=[]
	l=[]

	for i in range(n):
		uu=max(r[i],g[i],b[i])
		ll=min(r[i],g[i],b[i])
		u.append(uu)
		l.append(ll)
		m.append(r[i]+g[i]+b[i]-uu-ll)
	cu=0
	cm=0
	cl=0
	ans=1

	for i in range(n):
		while cu<=n-1 and u[n-1-cu]>m[n-1-i]:
			cu+=1
		while cl<=n-1 and l[cl]<m[i]:
			cl+=1
		ans=(ans*(i+1)*(cu-i)*(cl-i))%md
		'''
		print("cu  : ",cu)
		print("cl  : ",cl)
		print("i   : ",i)
		print("ans : ",ans)
		'''
	print(ans)
main()
