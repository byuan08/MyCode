import unittest
from 5_max_prize_places import get_max_number_of_summands

class Problem_5_TestCase(unittest.TestCase):
	""" Test Case for Problem 5 """

	def test_edge_case:
		ct,nums = get_max_number_of_summands(2,1)
		self.assertEqual(ct,1)
		self.assertEqual(num, [2])

if __name__ == "__main__":
	unittest.main()


