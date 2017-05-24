class QuickUnion(object):
	"""docstring for QuickUnion"""
	def __init__(self, num):
		super(QuickUnion, self).__init__()
		self.num = num
		self.id = range(num)
		self.sz = [1]*num

	def root(self, p):
		while p != self.id[p]:
			self.id[p] = self.id[self.id[p]]
			p = self.id[p]
		return p

	def connected(self, p, q):
		return self.root(p) == self.root(q)

	def union(self, p, q):
		i = self.root(p)
		j = self.root(q)
		if i == j:
			return
		if self.sz[i] > self.sz[j]:
			self.id[j] = i
			self.sz[i] += self.sz[j]
		else:
			self.id[i] = j
			self.sz[j] += self.sz[i]

	def display(self):
		print self.id

if __name__ == '__main__':
	QU = QuickUnion(10)
	QU.union(0,1)
	QU.union(2,4)
	QU.union(4,7)
	QU.union(0,7)
	print QU.connected(0,1),QU.connected(1,2)
	QU.display()