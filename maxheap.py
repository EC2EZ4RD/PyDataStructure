class maxheap(object):
	"""docstring for maxheap"""
	def __init__(self, items):
		super(maxheap, self).__init__()
		self.items = items
		self.lenth = len(items)
	
	def insert(self, num):
		self.items.append(num)
		self.lenth += 1
		index = self.lenth-1
		while index >= 1:
			if self.items[index] > self.items[index/2]:
				self.swap(index,index/2)
				index /= 2
			else:
				break
	
	def remove(self):
		self.swap(0, self.lenth)
		self.lenth -= 1
		self.items.pop()
		
	
	def sort(self):
		pass
	
	def swap(self, a, b):
		self.items[a], self.items[b] = self.items[b], self.items[a]

	def show(self):
		imax = 1		
		while imax < self.lenth:
			print self.items[imax/2:imax]
			imax = 2 * imax + 1
		print self.items[imax/2:self.lenth]

if __name__ == '__main__':
	a = [10,9,8,7,6,5,4,3,2]
	aheap = maxheap(a)
	print aheap.items
	print aheap.lenth
	aheap.show()
	aheap.insert(11)
	aheap.show()
	aheap.insert(12)
	aheap.show()
	aheap.insert(13)
	aheap.show()
	aheap.insert(14)
	aheap.show()
	aheap.insert(15)
	aheap.show()