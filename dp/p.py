class Solution24(object):
	ops = ["+", "-", "*", "/", "|-", "|/"]
	def operate(self, oprei, a, b):
		"""
		:type oprei: int, >=1 <=6
		:type a:int
		:type b:int
		:rtype: int
		"""
		if(oprei == 0):
			return a + b
		if(oprei == 1):
			return a - b
		if(oprei == 2):
			return a * b
		if(oprei == 3):
			if(b == 0 or (a%b) != 0):
				return None
			return a / b
		if(oprei == 4):
			return b - a
		if(oprei == 5):
			if(a == 0 or (b%a) != 0):
				return None
			return b / a;

	def loop(self, l):
		"""
        :type l: list
        :type sum: int
        :rtype: print
		"""
		n = len(l)
		if(n == 1 and l[0] == 24):
			return "True"
		m = len(self.ops)
		# dp = [[0] * n] * n
		for i in xrange(n):
			for j in xrange(i+1, n):
				for op in xrange(m):
					dp = self.operate(op, l[i], l[j])
					if(dp is None):
						continue
					# loop deeper	
					s = l[:]
					s.remove(l[i])
					s.remove(l[j])
					s.append(dp)
					if(self.loop(s) == "True"):
						print "{} {} {}".format(l[i], self.ops[op], l[j])
						return "True"
		return "False"
