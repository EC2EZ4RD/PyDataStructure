from Node import Node

class BSTNode(Node):
	"""docstring for BSTNode"""
	def __init__(self,  key, val, left = None, right = None, parent = None, heigth = 1):
		super(BSTNode, self).__init__(key, val, left, right, parent)
		self.heigth = heigth

class BST(object):
	"""docstring for BST"""
	def __init__(self, root = None):
		super(BST, self).__init__()
		self.root = root

	def insert_helper(self, h, parent, key, val):
		if h == None:
			return BSTNode(key, val, parent = parent, heigth = 1)
		c = key - h.key
		if c < 0:
			h.left = self.insert_helper(h.left, h, key, val)
		elif c > 0:
			h.right = self.insert_helper(h.right, h, key, val)
		else:
			h.val = val
			return h
		if h.left == None:
			lh = 0
		else:
			lh = h.left.heigth
		if h.right == None:
			rh = 0
		else:
			rh = h.right.heigth
		h.heigth = max(lh, rh) + 1
		return h

	def insert(self, key, val):
		self.root = self.insert_helper(self.root, None, key, val)

	def getHeight(self, key):
		if h == None:
			return 0
		h = self.getNode(key)
		return h.heigth

	def getNode(self, key):
		x = self.root
		while x != None:
			#c = key.compareTo(x.key)
			c = key - x.key
			if c < 0:
				x = x.left
			elif c > 0:
				x = x.right
			else:
				return x
		return None

	def getFarLeft(self, node):
		x = node
		while x.left != None:
			x = x.left
		return x

	def getFarRight(self, node):
		x = node
		while x.right != None:
			x = x.right
		return x

	def getVal(self, key):
		node = self.getNode(key)
		if node == None:
			return None
		return node.val

	def inorder_helper(self, node, layer):
		if node.left == None:
			pass
		else:
			self.inorder_helper(node.left,layer+1)
		if node.parent != None:
			print 'layer: #%d, key: %s, val: %s, parent: %s, heigth: %s '%(layer, node.key, node.val, node.parent.key, node.heigth)
		else:
			print 'layer: #%d, key: %s, val: %s, parent: %s, heigth: %s'%(layer, node.key, node.val, node.parent, node.heigth)
		if node.right == None:
			pass
		else:
			self.inorder_helper(node.right,layer+1)

	def inorder(self):
		self.inorder_helper(self.root,0)

	def contains(self, key):
		return self.getNode(key) != None

	def rank_helper(self, x, key):
		r = 0
		if x == None:
			return r
		c = key - x.key
		if c < 0:
			r = self.rank_helper(x.left, key)
		elif c == 0:
			r = self.rank_helper(x.left, key) + 1
		else:
			r = self.rank_helper(x.right, key) + self.rank_helper(x.left, key) + 1
		return r

	# nums of keys < key
	def rank(self, key):
		if self.contains(key):
			return self.rank_helper(self.root, key) - 1
		else:
			return self.rank_helper(self.root, key)

	# range in [a,b]
	def size(self, lo, hi):
		if self.contains(hi):
			return self.rank(hi) - self.rank(lo) + 1
		else: 
			return self.rank(hi) - self.rank(lo)

	def delete_helper(self, node, flag):
		if flag == 'left':
			if node.left == None:
				return node.right
			else:
				node.left = self.delete_helper(node.left, 'left')
				if node.left != None:
					node.left.parent = node
		elif flag == 'right':
			if node.right == None:
				return node.left
			else:
				node.right = self.delete_helper(node.right, 'right')
				if node.right != None:
					node.right.parent = node
		else:
			raise Exception('left or right error')

		if node.left == None:
			lh = 0
		else:
			lh = node.left.heigth
		if node.right == None:
			rh = 0
		else:
			rh = node.right.heigth
		node.heigth = max(lh, rh) + 1
		return node

	def delete2(self, key):
		if not self.contains(key):
			raise Exception("no such key");
		h = self.getNode(key)
		hparent = h.parent
		if h.left == None and h.right == None:
			if hparent.left == h:
				hparent.left = None
			else:
				hparent.right = None
			h = None
		elif h.left == None:
			if h == hparent.left:
				hparent.left = h.right
				h.right.parent = hparent
			else
				hparent.right = h.right
				h.right.parent = hparent
		elif h.right == None:
			if h == hparent.left:
				hparent.left = h.left
				h.left.parent = hparent
			else
				hparent.right = h.left
				h.left.parent = hparent


	def delete(self, key):
		if not self.contains(key):
			raise Exception("no such key");
		h = self.getNode(key)
		hparent = h.parent
		if h.left != None:
			victim = self.getFarRight(h.left)
			h.key, h.val = victim.key, victim.val
			h.left = self.delete_helper(h.left, 'right')
		elif h.right != None:
			victim = self.getFarLeft(h.right)
			h.key, h.val = victim.key, victim.val
			h.right = self.delete_helper(h.right, 'left')
		else:
			if hparent.left == h:
				hparent.left = None
			else:
				hparent.right = None
			h = None
		if h != None:
			if h.left == None:
				lh = 0
			else:
				lh = h.left.heigth
			if h.right == None:
				rh = 0
			else:
				rh = h.right.heigth
			h.heigth = max(lh, rh) + 1
		while hparent != None:
			if hparent.left == None:
				lh = 0
			else:
				lh = hparent.left.heigth
			if hparent.right == None:
				rh = 0
			else:
				rh = hparent.right.heigth
			hparent.heigth = max(lh, rh) + 1
			hparent = hparent.parent


if __name__ == '__main__':
	b = BST()
	b.insert(6,6)
	b.insert(2,2)
	b.insert(7,7)
	b.insert(0,0)
	b.insert(1,1)
	b.insert(5,5)
	b.insert(3,3)
	b.insert(4,4)
	b.inorder()
#	print b.contains(3)
#	print b.rank(0)
#	print b.rank(2.1)
#	print b.size(2.1,5)
	b.delete(6)
	print b.root
	b.inorder()