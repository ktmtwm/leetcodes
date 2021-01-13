class Solution(object):
	base = [1, 2, 3, 4, 5, 6, 7, 8, 9]
	n = len(base)
	result = None

	# def __init__(self, res):
	# 	self.res = res

	def judgeUnique(self, judge):
		"""
		:type  judge:list
		:rtype true/false
		"""
		lst = [0] * 10
		rows = len(judge)
		for i in range(rows):
			lst[int(judge[i])] += 1 
		for x in lst[1:]:
			if x > 1:
				return 0
		return 1

	def sub3_3_start(self, i):
		"""
		:rtype int
		"""
		return (i/3) * 3

	def isValid(self, res, x, y, num):
		"""
		:type res:[][], 9*9
		:type x,y:int
		:type num:int, 1-9
		"""
		res[x][y] = num
		#check line
		if not self.judgeUnique(res[x]):
			return 0
		#check colume
		colume = []
		for line in res:
			colume.append(line[y])
		if not self.judgeUnique(colume):
			return 0
		#chenck 3*3
		#line: xs:xs+3, column: ys:ys+3
		xs = self.sub3_3_start(x)
		ys = self.sub3_3_start(y)
		sub3_3 = []
		for i in range(xs, xs+3):
			for j in range(ys, ys+3):
				sub3_3.append(res[i][j])
		if not self.judgeUnique(sub3_3):
			return 0
		return 1

	def SudokuSolution(self, res):
		"""
		:type res:[][], 9*9
		"""
		self.result = None
		# while 0 in res[0]:
		# 	self.result = None
		# 	self.backtrack(res, 0)
		# 	res = self.result
		# for x in xrange(self.n):
		self.backtrack(res, 0, 0)

		return self.result

	def backtrack(self, res, row, column):

		if column == self.n:
			return

		if row == self.n:
			self.result = res
			return

		# if 0 not in res[row]:
		# 	self.backtrack(res, row+1, column)

		for y in xrange(self.n):
			if res[row][y] != 0:
				self.backtrack(res, row, y+1)
			# position row,y need to solute				
			for num in self.base:
				if not self.isValid(res, row, y, num):
					continue
				res[row][y] = num
				self.backtrack(res, row, y+1)
				if self.result is not None:
					return
				res[row][y] = 0

		self.backtrack(res, row+1, 0)

	# def backtrack(self, res, row):
	# 	if row == self.n:
	# 		self.result = res
	# 		return

	# 	# if 0 not in res[row]:
	# 	# 	self.backtrack(res, row+1)

	# 	for y in xrange(self.n):
	# 		# if res[row][y] != 0:
	# 		# 	continue
	# 		# position row,y need to solute				
	# 		org = res[row][y]
	# 		if org != 0:
	# 			for num in self.base:
	# 				if not self.isValid(res, row, y, num):
	# 					continue


	# 			# res[row][y] = num
	# 			org = res[row][y]
	# 			self.backtrack(res, row+1)
	# 			if self.result is not None:
	# 				return
	# 			res[row][y] = 0

if __name__ == '__main__':
	res = [[6, 0, 7, 0, 0, 0, 5, 1, 8],
		   [5, 1, 4, 6, 0, 8, 2, 3, 9],
		   [8, 2, 3, 5, 0, 1, 4, 6, 7],
		   [3, 6, 2, 7, 0, 9, 1, 8, 4],
		   [1, 7, 5, 8, 0, 2, 6, 9, 3],
		   [0, 0, 0, 0, 0, 0, 0, 0, 0],
		   [2, 4, 6, 9, 0, 5, 3, 7, 1],
		   [7, 3, 8, 1, 0, 4, 9, 5, 2],
		   [9, 5, 1, 2, 0, 7, 8, 4, 6]]
	print Solution().SudokuSolution(res)




