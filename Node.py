import key

class Node(object):
	"""docstring for Node"""
	#default color = BLACK in order to assure that when insert there is no AssertEXception because the first node color is black
	def __init__(self, key, val, left = None, right = None, parent = None):
		super(Node, self).__init__()
		self.key = key
		self.val = val
		self.left = left
		self.right = right
		self.parent = parent

	def hasParent(self):
		return self.parent != None

	def __hasLeftChild(self):
		return self.left != None

	def __hasRightChild(self):
		return self.right != None
	
	def hasChild(self):
		return self.__hasLeftChild() or self.__hasRightChild()

	def hasOneKid(self):
		return (self.__hasLeftChild() and not self.__hasRightChild()) or (self.__hasRightChild() and not self.__hasLeftChild())

	def hasTwoKids(self):
		return self.__hasLeftChild() and self.__hasRightChild()

	def getLeftChild(self):
		assert self.__hasLeftChild()
		return self.left

	def getLeftChild(self):
		assert self.__hasRightChild()
		return self.right

	def getParent(self):
		assert self.hasParent()
		return self.parent

	def getKey(self):
		return self.key

	def getVal(self):
		return self.value