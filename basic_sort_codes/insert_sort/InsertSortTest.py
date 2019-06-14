"""
"""
from InsertSort import InsertSortObj
import unittest

class InsertSortTestCase(unittest.TestCase):
	def setUp(self):
		"""
		DESC: init tested obj
		"""
		self.sort = InsertSortObj()

	def testEmptyList(self):
		"""
		DESC: sort empty list without error
		"""
		s = []
		self.sort.sort(s)

		self.assertEqual(s, [])

	def testSortedList(self):
		"""
		DESC: normal sort
		"""
		s = [-1, 2, 2, 3, 4, 55]
		self.sort.sort(s)

		self.assertEqual(s, s)

	def testReversedList(self):
		"""
		DESC: normal sort
		"""
		s = [55, 4, 3, 2, 2, -1]
		self.sort.sort(s)

		self.assertEqual(s, [-1, 2, 2, 3, 4, 55])

	def testLargeList(self):
		pass

def run_cases():
	suite = unittest.TestSuite()
	suite.addTest(InsertSortTestCase("testEmptyList"))
	suite.addTest(InsertSortTestCase("testSortedList"))
	suite.addTest(InsertSortTestCase("testReversedList"))
	return suite

if __name__ == "__main__":
	runner = unittest.TextTestRunner()
	runner.run(run_cases())
