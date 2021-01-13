class Solution(object):
	def __init__(self):
		self.res = []
		self.queen = 'Q'
		self.space = '.'

	def solveNQueens(self, n):
		"""
		:type n: int
		:rtype: List[List[str]]
		--------------------------
		Input: n = 4
		Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
		"""
		self.res = []
		self.n = n
		cb = []
		# init cb
		for i in xrange(n):
			s = []
			for j in xrange(n):
				s.append('.')
			cb.append(s)

		self.backtrack(cb, 0)
		return self.res

	def isValid(self, cb, x, y):
		"""
		:type cb:string[]
		:type x:int
		:type y:int
		"""
		#check row
		if self.queen in cb[x]:
			return 0
		#check column
		for cbi in cb:
			if self.queen in cbi[y]:
				return 0
		#check slash
		for i in range(self.n):
			for j in range(self.n):
				#+slash
				if (i-x) == (j-y) and self.queen in cb[i][j]:
					return 0
				#-slash
				if (i+j) == (x+y) and self.queen in cb[i][j]:
					return 0
		return 1

	def backtrack(self, cb, row):
		"""
		:type cb:string[]
		:type row:int
		"""
		if row == self.n:
			s = []
			for cbi in cb:
				s.append(''.join(cbi))
			self.res.append(s)
			return
		
		for x in xrange(self.n):
			if not self.isValid(cb, row, x):
				continue
			cb[row][x] = self.queen
			self.backtrack(cb, row+1)
			cb[row][x] = self.space
