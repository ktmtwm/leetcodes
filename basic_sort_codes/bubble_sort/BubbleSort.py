"""
"""

class BubbleSortObj(object):
	def sort(self, s):
		"""
		DESC: 	move the bigger one to right nearby,
				when there is no move action return.

				BETTER than select sort when sorted/part-sorted.
		PERFORMANCE: 
				o(n2),	average time cost
				o(n),	best time cost
				o(1),	space cost
		"""
		if len(s) < 2:
			return

		sorted_end_p = len(s) - 1
		while sorted_end_p > 0:
			inter_i = 0
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
				return
			sorted_end_p = sorted_end_p - 1
		# exit
		return
