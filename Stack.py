 class stack(object):
	"""docstring for stack"""
	def __init__(self):
		super(stack, self).__init__()
		self.space = []

	def insert(self, p):
		self.space.append(p)

	def remove(self, p):
		self.space.pop()

	def iterate(self):
		print self.space

	def size(self):
		return len(self.space)

	def isEmpty(self):
		return self.size() == 0

if __name__ == '__main__':
	a = stack()
	a.insert(1)
	a.remove(1)
	a.iterate()
	print a.isEmpty()
