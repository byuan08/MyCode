import unittest
from maximize_the_salary import *


class MSDTestCase(unittest.TestCase):
	
	def test_MSD_100(self):
		self.assertEqual(MSD(100),1)

	def test_MSD_1(self):
		self.assertEqual(MSD(1),1)

	def test_MSD_32(self):
		self.assertEqual(MSD(32),3)

	def test_MSD_0(self):
		self.assertRaises(ValueError, MSD, 0)

class RestFromMSDTestCase(unittest.TestCase):

	def test_100(self):
		self.assertEqual(rest_from_MSD(100), 0)

	def test_1(self):
		self.assertEqual(rest_from_MSD(1),0)

	def test_123(self):
		self.assertEqual(rest_from_MSD(123),23)

	def test_34(self):
		self.assertEqual(rest_from_MSD(34), 4)

class IsGreaterOrEqualTest(unittest.TestCase):
	def test_1(self):
		self.assertEqual(is_greater_or_equal(123,234),234)

	def test_2(self):
		self.assertEqual(is_greater_or_equal(111, 123), 123)

	def test_3(self):
		self.assertEqual(is_greater_or_equal(123, 32), 32)

	def test_4(self):
		self.assertEqual(is_greater_or_equal(100, 23), 23)

	def test_5(self):
		self.assertEqual(is_greater_or_equal(100, 10), 10)

	def test_6(self):
		self.assertEqual(is_greater_or_equal(123, 1), 1)

	def test_3(self):
		self.assertEqual(is_greater_or_equal(19, 1), 32)


if __name__ == '__main__':

	unittest.main()


