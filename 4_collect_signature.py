import sys

if __name__ == "__main__":
  n = int(sys.stdin.readline())
  segs = list()
  for i in range(n):
    
    # create tuple of each segment where 1st element is start point
    # and 2nd element is end point
    seg = tuple(map(int, sys.stdin.readline().split()))
    segs.append(seg)
  
  segs.sort(key = lambda tup:tup[1])
  
  
    
    
    
    
    
