import random
import numpy

class Sudoku(object):
	base = [1, 2, 3, 4, 5, 6, 7, 8, 9]
	n = len(base)
	s = numpy.zeros((n, n), int)
	retry = 0

	def ifRetry(self):
		"""
		:rtype true/false
		"""
		self.retry = self.retry + 1
		if self.retry > 50:
			return 0
		return 1
	
	def terminate(self):
		return self.retry > 50

	def reset(self):
		self.retry = 0
		self.s = numpy.zeros((self.n, self.n))

	def randomBase(self):
		random.shuffle(self.base)
		return self.base

	def judgeUnique(self, judge):
		"""
		:type  judge:list
		:rtype true/false
		"""
		lst = [0] * 10
		judge = judge.reshape(1, 9)
		[rows, cols] = judge.shape
		for i in range(rows):
			for j in range(cols):
				lst[int(judge[i, j])] += 1 
		for x in lst[1:]:
			if x > 1:
				return 0
		return 1

	def sub3_3_start(self, i):
		"""
		:rtype int
		"""
		return (i/3) * 3

	def berateRandom(self):
		while 1:
			self.reset()
			self.startLoopLine()
			if not self.terminate():
				print self.s
				break
		
	def startLoopLine(self):
		#line
		for i in xrange(self.n):
			self.loopLine(i)
			if self.terminate():
				return

	# linei generation
	def loopLine(self, i):
		if self.terminate():
			return

		self.s[i] = self.randomBase()
		print self.s[i]

		#column check
		for j in xrange(self.n):
			if not self.judgeUnique(self.s[:, j]):
				if not self.ifRetry():
					return
				self.loopLine(i)
		
		if self.terminate():
			return	
		#3*3 check
		xs = self.sub3_3_start(i)
		for j in xrange(3):
			if not self.judgeUnique(self.s[xs:xs+3, j:j+3]):
				if not self.ifRetry():
					return
				self.loopLine(i)

				
if __name__ == '__main__':
	Sudoku().berateRandom()


