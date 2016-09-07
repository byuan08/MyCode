#! python3
import sys

def dot_product(a, b):
	if len(a) > 0:
		return a.pop() * b.pop() + dot_product(a,b)
	else:
		return 0

if __name__ == "__main__":
	#print('main running')

	n = int(sys.stdin.readline())
	profit_per_click = list(map(int, sys.stdin.readline().split()))
	profit_per_click.sort()
	clicks_per_day = list(map(int, sys.stdin.readline().split()))
	clicks_per_day.sort()
	out = dot_product(profit_per_click, clicks_per_day)
	print(out)
