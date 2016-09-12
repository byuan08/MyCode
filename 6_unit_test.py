import unittest
from maximize_the_salary import *


class MSDTestCase(unittest.TestCase):
	
	def test_MSD_100(self):
		self.assertEqual(MSD(100),1)

	def test_MSD_1(self):
		self.assertEqual(MSD(1),1)

	def test_MSD_0(self):
		self.assertRaises(ValueError, MSD, 0)

class RestFromMSDTestCase(unittest.TestCase):

	def test_100(self):
		self.assertEqual(rest_from_MSD, 0)

	def test_1(self):
		self.assertEqual(rest_from_MSD(1),0)

	def test_123(self):
		self.assertEqual(rest_from_MSD(123),23)

	def test_34(self):
		self.assertEqual(rest_from_MSD(34), 4)

if __name__ == '__main__':

	unittest.main()


