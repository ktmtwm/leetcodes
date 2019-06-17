"""
"""

class CockTailSortObj(object):
	def sort(self, s):
		"""
		DESC: 	Better than bubble because it sorts moving forwards and backwards

				BETTER than select sort when sorted/part-sorted.
		PERFORMANCE: 
				o(n2),	average time cost
				o(n),	best time cost
				o(1),	space cost
		"""
		if len(s) < 2:
			return

		sorted_end_p = len(s) - 1
		sorted_start_p = 0
		while sorted_start_p < sorted_end_p:
			if self.inter_forwards(s, sorted_start_p, sorted_end_p):
				# no exchange exit
				return
			if self.inter_backwards(s, sorted_start_p, sorted_end_p):
				# no exchange exit
				return
		# exit
		return

	def inter_forwards(self, s, sorted_start_p, sorted_end_p):
		"""
		"""
		inter_i = sorted_start_p
		exchanged = 0

		while inter_i < sorted_end_p:
			# compare value(i) && value(i+1), move the bigger one to i+1
			if s[inter_i] > s[inter_i + 1]:
				exchanged = 1
				# exchange i, i+1
				tmp = s[inter_i]
				s[inter_i] = s[inter_i + 1]
				s[inter_i + 1] = tmp

			inter_i = inter_i + 1

		# exit
		if not exchanged:
			return 1
		sorted_end_p = sorted_end_p - 1
		return 0

	def inter_backwards(self, s, sorted_start_p, sorted_end_p):
		"""
		"""
		inter_i = sorted_end_p
		exchanged = 0

		while inter_i > sorted_start_p:
			# compare value(i) && value(i-1), move the smaller one to i-1
			if s[inter_i] < s[inter_i - 1]:
				exchanged = 1
				# exchange i, i-1
				tmp = s[inter_i]
				s[inter_i] = s[inter_i - 1]
				s[inter_i - 1] = tmp

			inter_i = inter_i - 1

		# exit
		if not exchanged:
			return 1
		sorted_start_p = sorted_start_p - 1
		return 0
