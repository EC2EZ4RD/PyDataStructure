import Node
RED = True
BLACK = False

class RBNode(Node.Node):
	"""docstring for RBNode"""
	def __init__(self, key, val, left = None, right = None, parent = None, color = BLACK):
		super(RBNode, self).__init__(key, val, left, right, parent)
		self.color = color
		
class RBT(object):
	"""docstring for RBT"""
	def __init__(self, root = None):
		super(RBT, self).__init__()
		self.root = root

	def isRed(self, x):
		if x == None:
			return False
		return x.color == RED

	#in fact the BST search
	def get(self, key):
		x = self.root
		while x != None:
			#c = key.compareTo(x.key)
			c = key - x.key
			if c < 0:
				x = x.left
			elif c > 0:
				x = x.right
			else:
				return x.val
		return None

	#right-lean to left-lean
	def rotateLeft(self, h):
		assert self.isRed(h.right)
		print 'rl'
		x = h.right
		h.right = x.left
		if x.left != None:
			x.left.parent = h
		x.left = h
		x.parent = h.parent
		h.parent = x
		x.color = h.color
		h.color = RED
		return x

	#left-lean to right-lean
	def rotateRight(self, h):
		assert self.isRed(h.left)
		print 'rr'
		x = h.left
		h.left = x.right
		if x.right != None:
			x.right.parent = h
		x.right = h
		x.parent = h.parent
		h.parent = x
		x.color = h.color
		h.color = RED
		return x

	#two kids are both red to parent is red
	def flipColors(self, h):
		if h == self.root:
			pass
		else:
			assert self.isRed(h) == False
		assert self.isRed(h.left)
		assert self.isRed(h.right)
		print 'flip'
		h.color = RED
		h.left.color = BLACK
		h.right.color = BLACK
		return h

	#iterate bottom-up
	def put(self, h, parent, key, val):
		if h == None:
			return RBNode(key, val, parent = parent, color = RED)
		#c = key.compareTo(h.key)
		c = key-h.key
		if c < 0:
			h.left = self.put(h.left, h, key, val)
		elif c > 0:
			h.right = self.put(h.right, h, key, val)
		else:
			h.val = val
		if self.isRed(h.right) and self.isRed(h.left) == False:
			h = self.rotateLeft(h)
		if self.isRed(h.left) and self.isRed(h.left.left):
			h = self.rotateRight(h)
		if self.isRed(h.left) and self.isRed(h.right):
			h = self.flipColors(h)

		if h == self.root:
			h.color = BLACK
			h.parent = None
		return h

	def insert(self, key, val):
		self.root = self.put(self.root, None, key, val)

	def inorder_helper(self, node, layer):
		if node.left == None:
			pass
		else:
			self.inorder_helper(node.left,layer+1)
		if node.parent != None:
			print 'layer: #%d, key: %s, color: %s, parent: %s '%(layer,node.key,node.color,node.parent.key)
		else:
			print 'layer: #%d, key: %s, color: %s, parent: %s '%(layer,node.key,node.color,node.parent)
		if node.right == None:
			pass
		else:
			self.inorder_helper(node.right,layer+1)

	def inorder(self):
		self.inorder_helper(r.root,0)

	def delete(self, key):
		x = self.root
		while x != None:
			#c = key.compareTo(x.key)
			c = key - x.key
			if c < 0:
				x = x.left
			elif c > 0:
				x = x.right
			else:
				break
		if x == None:
			return
		if x.hasTwoKids():
			tmp = x.right
			while tmp.left != None:
				tmp = tmp.left
			x.key = n.key
			x.val = n.val
			#there maybe exist a problem
			x = tmp
		if not x.hasChild():
			if x.color == RED:
				x = None
			else:
				pass

		else:
			pass




		#x is the node to be deleted
		tmp = x.right
		if tmp == None:
			n = x
		else:
			while tmp.left != None:
				tmp = tmp.left
			n = tmp
		#n is the node to fill the place

		x.key = n.key
		x.val = n.val

		#delete n
		#n is root
		if n.parent == None:
			n = None
			return

'''
		#n is not root
		if n.parent != None:
			nparent = n.parent
			if n.parent.left == n:
				pass
			else:
				if n.hasChild():
					n.parent.right = n.left
					n.left.parent = n.parent
					n.left.color = BLACK
					n = None
				else:
					ncousin = nparent.left
					if ncousin.hasChild():

					else:
						ncousin.color = RED
					n.parent.right = None
				#

				return
		else:
			n = None
			return

		if n.color == RED:
			n = None
			return
		else:
			if nparent.right.hasChild():
				n = None
				nparent.right.color == RED
				nparent = self.rotateLeft(nparent)
				nparent.left = self.rotateLeft(nparent.left)
				nparent = self.rotateRight(nparent)
				nparent = self.flipColors(nparent)
			else:
				if nparent.color == RED:
'''



if __name__ == '__main__':
	r = RBT(RBNode(0,0))
	r.insert(1,1)
	r.insert(2,2)
	r.insert(3,3)
	r.insert(4,4)
	r.insert(5,5)
	r.insert(6,6)
	r.insert(7,7)
	#print r.root.left
	#print r.root.right
	r.inorder()