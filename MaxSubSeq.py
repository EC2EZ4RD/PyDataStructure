#coding=utf-8
#有深拷贝和浅拷贝的原因

def MaxSubSeq(x):
	lenth = len(x)
	G_M = [0,0]
	S_M = [0,0]
	for i in range(lenth):
		if x[i] + sum(x[S_M[0]:S_M[1]]) > sum(x[G_M[0]:G_M[1]]):
			S_M[1] += 1
			G_M[0],G_M[1] = S_M[0],S_M[1]
		elif x[i] + sum(x[S_M[0]:S_M[1]]) > 0:
			S_M[1] += 1
		else:
			S_M = [i+1,i+1]
	return G_M

if __name__ == '__main__':
	a = [2,-3,1.5,-1,3,-2,-3,3]
	G_M = MaxSubSeq(a)
	print G_M
	print sum(a[G_M[0]:G_M[1]])