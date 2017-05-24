#coding=utf-8
import random
import time  
  
def timeit(func):  
    def wrapper(*args):  
        start = time.clock()  
        func(*args)  
        end =time.clock()  
        print args[0].__name__,'used:', end - start  
    return wrapper

class Insertation(object):
	"""docstring for Insertation"""
	def __init__(self):
		super(Insertation, self).__init__()

	@classmethod
	def sort(cls, a):
		cls.sort_helper(a,0,len(a)-1)

	@classmethod
	def sort_helper(cls, a, lo, hi):
		for p in range(lo, hi+1):
			mi = a[p]
			k = p
			for q in range(p+1,hi+1):
				if a[q] < mi:
					k = q
					mi = a[q]
			a[p],a[k] = a[k],a[p]

	@classmethod
	def binary_sort(cls, a):
		cls.binary_sort_helper(a,0,len(a)-1)

	@classmethod
	def binary_sort_helper(cls, a, lo, hi):
		if hi <= lo:
			return
		cls.binary_sort_helper(a, lo, hi-1)
		if a[hi] >= a[hi-1]:
			return
		elif a[hi] <= a[lo]:
			a[lo],a[lo+1:hi+1] = a[hi],a[lo:hi]
		else:
			mid = cls.binary_search(a, lo, hi, a[hi])
			a[mid],a[mid+1:hi+1] = a[hi],a[mid:hi]

	@classmethod
	def binary_search(cls, a, lo, hi, key):
		while hi >= lo:
			mid = (lo + hi) / 2
			if a[mid] == key:
				return mid
			elif a[mid] < key:
				lo = mid + 1
			else:
				hi = mid - 1
		return lo

class ShellSort(object):
	"""docstring for ShellSort"""
	def __init__(self):
		super(ShellSort, self).__init__()

	@classmethod
	def sort(cls, a):
		lenth = len(a)
		h = 1
		while h < lenth/3:
			h = 3*h + 1
		while h >= 1:
			for i in range(h,lenth):
				j = i
				while j >= h and a[j] < a[j-h]:
					a[j],a[j-h] = a[j-h],a[j]
					j -= h
			h /= 3

class Merge(object):
	"""docstring for Merge"""
	CUTOFF = 5

	def __init__(self):
		super(Merge, self).__init__()

	@classmethod
	def merge(cls, a, aux, lo, mid, hi):
		#assert self.isSorted(a,lo,mid)
		#assert self.isSorted(a,mid+1,hi)
		for index in range(lo,hi+1):
			aux[index] = a[index]
		p = lo
		q = mid + 1
		index = lo
		#此处还不能将条件合并
		for index in range(lo,hi+1):
			if p > mid:
				a[index] = aux[q]
				q += 1
			elif q > hi:
				a[index] = aux[p]
				p += 1
			elif aux[p] > aux[q]:
				a[index] = aux[q]
				q += 1
			else:
				a[index] = aux[p]
				p += 1
		#assert self.isSorted(a,lo,hi)

	@classmethod
	def sort_helper(cls, a, aux, lo, hi):
		if hi <= lo + cls.CUTOFF - 1:
			Insertation.sort_helper(a,lo,hi)
			return
		if hi <= lo:
			return
		mid = (hi+lo)/2
		cls.sort_helper(a,aux,lo,mid)
		cls.sort_helper(a,aux,mid+1,hi)
		if a[mid] <= a[mid+1]:
			return
		cls.merge(a,aux,lo,mid,hi)

	
	@classmethod
	def sort(cls, a):
		aux = [None] * len(a)
		cls.sort_helper(a,aux,0,len(a)-1)

	def isSorted(self, a, lo, hi):
		for i in range(lo,hi):
			if a[lo]>a[hi]:
				return False

class QuickSort(object):
	"""docstring for QuickSort"""
	CUTOFF = 3

	def __init__(self):
		super(QuickSort, self).__init__()

	@classmethod
	def shuffle(cls, a):
		lenth = len(a)
		for i in range(lenth):
			k = random.randint(i,lenth-1)
			a[i],a[k] = a[k],a[i]

	@classmethod
	def medianOf3(cls, a, lo, hi):
		if a[lo]>a[hi]:
			a[lo],a[hi] = a[hi],a[lo]
		if a[(lo+hi)/2] > a[hi]:
			a[lo],a[hi] = a[hi],a[lo]
		elif a[(lo+hi)/2] < a[lo]:
			return
		else:
			a[lo],a[(lo+hi)/2] = a[(lo+hi)/2],a[lo]

	@classmethod
	def partition(cls, a, lo, hi):
		i = lo + 1
		j = hi
		while True:
			while a[i]<a[lo]:
				i += 1
				if i >= hi:
					break
			#in fact "if j<=lo then break" is redundant becasue j will count down to lo, then a[j] = a[lo], then break
			while a[j]>a[lo]:
				j -= 1
				if j <= lo:
					break
			if i>=j:
				break
			a[i],a[j] = a[j],a[i]
		a[lo],a[j] = a[j],a[lo]
		return j

	@classmethod
	def threeway(cls, a, lo, hi):
		lt = lo
		gt = hi
		i = lt
		#此处一定要有v=a[lo]，因为下面的步骤会改变a[lo]的值，就无法作为pivot
		v = a[lo]
		while i <= gt:
			if  a[i] < v:
				a[lt],a[i] = a[i],a[lt]
				lt += 1
				i +=1
			elif a[i] > v:
				a[gt],a[i] = a[i],a[gt]
				gt -= 1
			else:
				i += 1

		return lt,gt

	@classmethod
	def sort_helper(cls, a, lo, hi):
		if hi <= lo:
			return
		#if hi <= lo + cls.CUTOFF - 1:
		#	Insertation.sort_helper(a, lo, hi)
		#	return
		(lt,gt) = cls.threeway(a, lo, hi)
		cls.sort_helper(a, lo, lt-1)
		cls.sort_helper(a, gt+1, hi)
		#j = cls.partition(a, lo, hi)
		#cls.sort_helper(a, lo, j-1)
		#cls.sort_helper(a, j+1, hi)

	
	@classmethod
	def sort(cls, a):
		#cls.medianOf3(a,0,len(a)-1)
		#cls.shuffle(a)
		cls.sort_helper(a,0,len(a)-1)

	@classmethod
	def select(cls, a, k):
		cls.shuffle(a)
		lo = 0
		hi = len(a)-1
		assert k >= lo and k <= hi
		while lo < hi:
			j = QuickSort.partition(a, lo, hi)
			if j < k:
				lo = j + 1
			elif j > k:
				hi = j - 1
			else:
				return a[k]
		return a[k]

class HeapSort(object):
	"""docstring for HeapSort"""
	def __init__(self):
		super(HeapSort, self).__init__()
	
	@classmethod
	def sink(cls, a, k, N):
		while 2*k + 1<= N:
			j = 2 * k + 1
			if j < N and a[j] < a[j+1]:
				j += 1
			if a[k] <= a[j]:
				a[k],a[j] = a[j],a[k]
			k = j

	@classmethod
	def sort(cls, a):
		lenth = len(a)
		N = lenth - 1
		for k in range(lenth/2,-1,-1):
			cls.sink(a,k,N)
		#以上已经建立好最大堆
		while N>0:
			a[0],a[N] = a[N],a[0]
			N -= 1
			cls.sink(a,0,N)

	@classmethod
	def initial(cls, a):
		lenth = len(a)
		N = lenth - 1
		for k in range(lenth/2,-1,-1):
			cls.sink(a,k,N)
@timeit
def sort(cls, a):
	cls.sort(a)

if __name__ == '__main__':
	
	a = range(1000000)
	b = range(1000000)
	c = range(1000000)
	d = range(1000000)
	QuickSort.shuffle(a)
	QuickSort.shuffle(b)
	QuickSort.shuffle(c)
	QuickSort.shuffle(d)
	#sort(Insertation, a)
	sort(QuickSort, a)
	sort(Merge, b)
	sort(ShellSort, c)
	sort(HeapSort, d)
	#print a
	#print b
	#print c
	#print d