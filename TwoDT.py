from Point import Point

Vert = True
Hori = False

class TwoDTNode(Point):
	"""docstring for TwoDTNode"""
	def __init__(self, x, y, left = None, right = None, parent = None, direct = Vert):
		super(TwoDTNode, self).__init__(x, y)
		self.left = left
		self.right = right
		self.parent = parent
		self.direct = direct
		

class TwoDT(object):
	"""docstring for TwoDT"""
	def __init__(self, root = None):
		super(TwoDT, self).__init__()
		self.root = root
		
	def insert_helper(self, h, parent, x, y, direct):
		if h == None:
			return TwoDTNode(x, y, direct = direct)
		if h.direct == Vert:
			c = x - h.x
			if c < 0:
				h.left = self.insert_helper(h.left, h, x, y, Hori)
			elif c > 0:
				h.right = self.insert_helper(h.left, h, x, y, Hori)
			else:
				h.x, h.y = x, y
		else:
			c = y - h.y
			if c < 0:
				h.left = self.insert_helper(h.left, h, x, y, Vert)
			elif c > 0:
				h.right = self.insert_helper(h.right, h, x, y, Vert)
			else:
				h.x, h.y = x, y
		return h

	def insert(self, x, y):
		self.root = self.insert_helper(self.root, None, x, y, Vert)

	def inorder_helper(self, node, layer):
		if node.left == None:
			pass
		else:
			self.inorder_helper(node.left,layer+1)
		if node.parent != None:
			print 'layer: #%d, (x,y): (%s,%s), direction: %s, parent: %s'%(layer, node.x, node.y, node.direct, node.parent.key)
		else:
			print 'layer: #%d, (x,y): (%s,%s), direction: %s, parent: %s'%(layer, node.x, node.y, node.direct, node.parent)
		if node.right == None:
			pass
		else:
			self.inorder_helper(node.right,layer+1)

	def inorder(self):
		self.inorder_helper(self.root,0)

	def find_helper(self, h, x1, y1, x2, y2, plist):
		if h == None:
			return
		print (h.x,h.y)
		if h.x >= x1 and h.x <= x2 and h.y >= y1 and h.y <= y2:
			plist.append((h.x,h.y))
		self.find_helper(h.left, x1, y1, x2, y2, plist)
		self.find_helper(h.right, x1, y1, x2, y2, plist)

	def find(self, x1, y1, x2, y2):
		plist = []
		self.find_helper(self.root, x1, y1, x2, y2, plist)
		return plist

	def closest_helper(self, h, x, y, pmin, dmin):
		if h == None:
			return pmin
		curDis = (x - h.x)**2 + (y - h.y)**2
		if curDis < dmin:
			dmin = curDis
			pmin = h
		if (h.direct == Vert and x < h.x) or (h.direct == Hori and y < h.y):
			pmin = self.closest_helper(h.left, x, y, pmin, dmin)
		else:
			pmin = self.closest_helper(h.right, x, y, pmin, dmin)
		straightDis = (x - h.x)**2 if h.direct == Vert else (y - h.y)**2
		if straightDis > dmin:
			return pmin
		if (h.direct == Vert and x < h.x) or (h.direct == Hori and y < h.y):
			pmin = self.closest_helper(h.left, x, y, pmin, dmin)
		else:
			pmin = self.closest_helper(h.right, x, y, pmin, dmin)
		return pmin

	def closest(self, x, y):
		return self.closest_helper(self.root, x, y, None, float('inf'))

if __name__ == '__main__':
	a = TwoDT()
	a.insert(5,5)
	a.insert(7,4)
	a.insert(3,6)
	a.insert(2,1)
	a.insert(1,4)
	a.inorder()
	print a.find(1,2,10,10)
	print a.closest(1,1).x,a.closest(1,1).y