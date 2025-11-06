from heapq import heappush as P, heappop as R
N,W=map(int,input().split())
A=[]
L=[]
for _ in range(N):
	g,s=map(int,input().split())
	P(A,g)
	P(L,g+s)
S=0
l=R(L)
a=R(A)
try:
	while True:
		if a>=l:
			if a-l<=W:
				S+=1
				a=R(A)
			l=R(L)
		else:a=R(A)
except:
	print(S)