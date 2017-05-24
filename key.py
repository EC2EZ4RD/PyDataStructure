#you can define your own key
#just need to rewrite the compareTo()
class key(object):
	"""docstring for key"""
	def __init__(self, arg):
		super(key, self).__init__()
		self.arg = arg

	def compareTo(self, that):
		return self.arg - that.arg