class MinPQ(object):
	"""docstring for MinPQ"""
	def __init__(self, pq):
		super(MinPQ, self).__init__()
		self.pq = pq

	def isEmpty():
		return len(self.pq) <= 0

	def insert(self, key):
		self.pq.append(key)
		self.swim(len(self.pq)-1)

	def delMin():
		self.exch(0, len(self.pq)-1)
		key = self.pq.pop()
		self.sink(0)
		return key

	def swim(self, k):
		while k > 1 and self.less(k/2, k):
			self.exch(k/2, k)
			k = k/2

	def sink(self, k):
		N = len(self.pq) - 1
		while 2*k + 1<= N:
			j = 2 * k + 1
			if j < N and a[j] < a[j+1]:
				j += 1
			if a[k] <= a[j]:
				a[k],a[j] = a[j],a[k]
			k = j

	def less(self, i, j):
		return pq[i].compareTo(p[j]) < 0

	def exch(self, i, j):
		pq[i],pq[j] = pq[j],pq[i]