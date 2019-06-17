"""
"""
from SelectSort import SelectSortObj
import unittest

class SelectSortTestCase(unittest.TestCase):
	def setUp(self):
		"""
		DESC: init tested obj select_sort_obj
		"""
		self.select_sort = SelectSortObj()

	def testEmptyList(self):
		"""
		DESC: sort empty list without error
		"""
		s = []
		self.select_sort.sort(s)

		self.assertEqual(s, [])

	def testSortedList(self):
		"""
		DESC: normal sort
		"""
		s = [-1, 2, 2, 3, 4, 55]
		self.select_sort.sort(s)

		self.assertEqual(s, s)

	def testReversedList(self):
		"""
		DESC: normal sort
		"""
		s = [55, 4, 3, 2, 2, -1]
		self.select_sort.sort(s)

		self.assertEqual(s, [-1, 2, 2, 3, 4, 55])
		
	def testNormalList(self):
		"""
		DESC: normal sort
		"""
		s = [-2, 4, 55, 2, 2, -1]
		self.sort.sort(s)

		self.assertEqual(s, [-2, -1, 2, 2, 4, 55])

	def testLargeList(self):
		pass

def run_cases():
	suite = unittest.TestSuite()
	suite.addTest(SelectSortTestCase("testEmptyList"))
	suite.addTest(SelectSortTestCase("testSortedList"))
	suite.addTest(SelectSortTestCase("testReversedList"))
	suite.addTest(SelectSortTestCase("testNormalList"))
	return suite

if __name__ == "__main__":
	# unittest.main(defaultTest = 'run_cases')
	runner = unittest.TextTestRunner()
	runner.run(run_cases())
