import sys

def get_max_loot_value(Capacity, item_sorted):
	item = item_sorted.pop()
	w = item[0]
	unit_value = item[1]
	print("w is: ", w)
	print("uvalue is: ", unit_value)
	if w <= Capacity:
		Capacity = Capacity - w
		#item_sorted.pop()
		return w * unit_value + get_max_loot_value(Capacity, item_sorted)

	else:

		return Capacity * unit_value



#if __name__ == "__main__":
print('running main')
line1 = list(map(int, sys.stdin.readline().split()))
n = line1[0]
W = line1[1]
print(W)
value = list()
items = list()

for i in range(n):
	line = list(map(int, sys.stdin.readline().split()))
	value = line[0]
	weight = line[1]
	unit_value = float(value/weight)
	items.append((weight, unit_value))

items.sort(key = lambda tup: tup[1])
print(items)

print(get_max_loot_value(W, items))



    
  
    
  
  
  
