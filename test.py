class A(object):
	"""docstring for A"""
	def __init__(self, arg):
		super(A, self).__init__()
		self.arg = arg
		

def function(a):
	a[0] = A(8)

if __name__ == '__main__':
	a = [A(6)]
	print id(a[0].arg)
	print a[0].arg
	function(a)
	print id(a)
	print id(a[0].arg)
	print a[0].arg
	print id(a)