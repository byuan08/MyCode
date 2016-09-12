import sys
from math import log10, floor

n_digit = lambda x: floor(log10(x))
def MSD(x): return x / 10 ** n_digit(x)
def rest_from_MSD(x): return x % 10 ** n_digit(x)

def is_greater_or_equal(m,n):
	''' this function returns the number with greater MSD.
	If the two inputs have the same MSD, the function will 
	return the one with greater 2nd MSD'''
	
	if MSD(m) > MSD(n): return m
	
	elif MSD(m) < MSD(n): return n

	else: 
		return is_greater_or_equal(rest_from_MSD(m), rest_from_MSD(n))