from BST import BST

class IntervalSTNode(object):
	"""docstring for IntervalSTNode"""
	def __init__(self, lo, hi, val):
		super(IntervalSTNode, self).__init__()
		self.lo = lo
		self.hi = hi
		self.val = val

class IntervalST(BST):
	"""docstring for IntervalST"""
	def __init__(self, root = None):
		super(IntervalST, self).__init__(root)


	def put(self, lo, hi, val):
		self.insert(lo,(lo,hi,val))

	def get(self, lo, hi):
		node = self.getVal(lo)
		if node[1] == hi:
			return val
		return None
		
	def delete(self, lo, hi):
		pass

	def intersects(self, lo, hi):
		pass



if __name__ == '__main__':
	a = IntervalST()
	a.put(1,3,'a')
	a.put(2,5,'b')
	a.inorder()