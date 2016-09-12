#! /usr/local/bin/python3
import sys

def get_max_number_of_summands(n, l):
	summands = []

	if n < l:
		print('The input has to be interger bigger than 0')
		return []
		print("case 1")

	while (True):
		if n > 2*l:
			summands.append(l)
			n -= l
			l += 1
			#print ("case 3,  n = {}, l = {}, summands = {}".format(n, l, summands))
			continue
			
		else:
			summands.append(n)
			#print("case 2,  n = {}, l = {}, summands = {}".format(n, l, summands))
			return summands
	
if __name__ == "__main__":
	print('running main')
	n = int(sys.stdin.readline())
	print("n= ",n)
	summands = get_max_number_of_summands(n, 1)
	print(len(summands))
	for x in summands:
		#print(x, end=' ')
