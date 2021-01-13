import random
import numpy

class Sudoku(object):
	base = [1, 2, 3, 4, 5, 6, 7, 8, 9]
	n = len(base)
	s = numpy.zeros((n, n), int)
	retry = 0
	maxRetry = 110

	def ifRetry(self):
		"""
		:rtype true/false
		"""
		self.retry = self.retry + 1
		if self.retry > self.maxRetry:
			return 0
		return 1
	
	def terminate(self):
		return self.retry > self.maxRetry

	def reset(self):
		self.retry = 0
		self.s = numpy.zeros((self.n, self.n), int)

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
				print "-------END-------"
				print self.s
				break
		
	def startLoopLine(self):
		#line
		for i in xrange(self.n):
			print "setting: " + str(i)
			while not self.setLine(i):
				if not self.ifRetry:
					break

			if self.terminate():
				return
			
	# linei generation
	def setLine(self, i):
		self.s[i] = self.randomBase()

		#column check
		for j in xrange(self.n):
			if not self.judgeUnique(self.s[:, j]):
				return 0

		#3*3 check
		xs = self.sub3_3_start(i)
		for j in xrange(3):
			if not self.judgeUnique(self.s[xs:xs+3, j*3:j*3+3]):
				return 0

		return 1
				
if __name__ == '__main__':
	Sudoku().berateRandom()


