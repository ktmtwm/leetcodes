
class ElemRepetitionCountObj(object):
	def elem_count(self, s):
		"""
		DESC: s , [] list of int
		OUTPUT: dict()
				key, elements in s 
				value, repetition count
		Performance:
				o(n) 	time cost
				o(n)	space cost
		"""
		rep_count = dict()

		for i in s:
			rep_count[i] = rep_count.get(i, 0) + 1

		return rep_count


