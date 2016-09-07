import os

def dot_product(a, b):
  if len(a) > 0:
    return a.pop() * b.pop() + dot_product(a,b)
  else:
    return 0

if __name__ == "__main__":
  n = int(os.stdin.readline())
  profit_per_click = list(map(int, os.stdin.readline().split())).sort()
  clicks_per_day = list(map(int, os.stdin.readline().split())).sort()
  out = dot_product(a, b)
  print(out)
  
  
