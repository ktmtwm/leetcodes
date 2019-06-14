"""
"""

class SelectSortObj(object):
	def sort(self, s):
		sorted_i = 0
		inter_j = 0

		while sorted_i < len(s):
			smallist_j = inter_j

			# the smallest
			while inter_j < len(s):
				if s[inter_j] < s[smallist_j]:
					smallist_j = inter_j
				inter_j = inter_j + 1
								
			# exchange
			tmp = s[smallist_j]
			s[smallist_j] = s[sorted_i]
			s[sorted_i] = tmp

			# continue
			sorted_i = sorted_i + 1
			inter_j = sorted_i
