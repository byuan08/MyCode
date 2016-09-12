import unittest
from maximize_the_salary import MSD


class MyTestCase(unittest.TestCase):
	
	def test_number_of_digit_100(self):
		self.assertEqual(MSD(100),1)

	def test_number_of_digit_1(self):
		self.assertEqual(MSD(1),1)

	def test_number_of_digit_0(self):
		
		self.assertRaises(ValueError, self.assertEqual(MSD(0),0))

if __name__ == '__main__':

	unittest.main()


