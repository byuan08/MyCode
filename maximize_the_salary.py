import sys
from math import log10, floor

n_digit = lambda x: floor(log10(x))
def MSD(x): return int(x / 10 ** n_digit(x))
def rest_from_MSD(x): return x % 10 ** n_digit(x)


def is_greater_or_equal(m,n):
	''' this function returns the number with greater MSD.
	If the two inputs have the same MSD, the function will 
	return the one with greater 2nd MSD'''
	
	if MSD(m) > MSD(n): return m
	
	elif MSD(m) < MSD(n): return n

	else: 
		#if :


		return is_greater_or_equal(rest_from_MSD(m), rest_from_MSD(n))

# '''
# 41 % 10 = (4,1)
# 40 % 10 = (4,0)
# 4 % 10 =  (0,4)
# '''

# def is_greater_or_equal(m,n):

# 	str_m = str(m)
# 	str_n = str(n)
# 	digits_m = len(str_m)
# 	digits_n = len(str_n)

# 	if int(str_m[digits_m]) < int(str_n[digits_n]):

# 		return n

# 	if int(str_m[digits_m]) > int(str_n[digits_n]):

# 		return m

# 	if int(str_m[digits_m]) = int(str_n[digits_n]):

		





