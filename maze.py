class maze(object):
	"""docstring for maze"""
	def __init__(self, num):
		super(maze, self).__init__()
		self.num = num
		self.id = range(num*num)
		self.sz = [1] * num*num

	def root(self, p):
		while p != self.id[p]:
			self.id[p] = self.id[self.id[p]]
			p = self.id[p]
		return p

	def up(self, p):
		if p <= self.num:
			return None
		else:
			return p - self.num

	def down(self, p):
		if p > self.num * self.num - self.num:
			return None
		else:
			return p + self.num

	def left(self, p):
		if p % self.num == 0:
			return None
		else:
			return p - 1

	def right(self, p):
		if p % self.num == self.num-1:
			return None
		else:
			return p + 1

	def union(self, p, q):
		i = self.root(p)
		j = self.root(q)
		if i == j:
			return
		if self.sz[i] < self.sz[j]:
			self.id[i] = j
			self.sz[j] += self.sz[i]
		else:
			self.id[j] = i
			self.sz[i] += self.sz[j]

	def display(self):
		for i in range(self.num):
			print self.id[i*self.num:(i+1)*self.num]

if __name__ == '__main__':
	m = maze(5)
	m.union(1,m.down(1))
	m.union(1,m.right(1))
	m.display()