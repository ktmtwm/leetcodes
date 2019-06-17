
from ElemRepetitionCount import ElemRepetitionCountObj
import unittest

class ElemRepetitionCountObjTestCase(unittest.TestCase):
	def setUp(self):
		self.count = ElemRepetitionCountObj()

	def testEmptyList(self):
		s = []
		count_s = self.count.elem_count(s)

		self.assertDictEqual(count_s, {})

	def testNormalList(self):
		s = [-1, -1, 2, 4, 7, 4, 10, 9]
		count_s = self.count.elem_count(s)

		self.assertDictEqual(count_s, {
			-1 : 2,
			2  : 1,
			4  : 2,
			7  : 1,
			10 : 1,
			9  : 1,
			})

	def testLargeList(self):
		pass

def run_cases():
	suite = unittest.TestSuite()
	suite.addTest(ElemRepetitionCountObjTestCase("testEmptyList"))
	suite.addTest(ElemRepetitionCountObjTestCase("testNormalList"))
	return suite

if __name__ == "__main__":
	run = unittest.TextTestRunner()
	run.run(run_cases())

