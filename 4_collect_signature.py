
#! python3
import sys

def get_min_points_to_cover_segments(n, segments):
  if len(segments) > 0:
    count ++
    endpoint_cur = segments.pop()[1]
    for x in segments
      # Only check the points whose start point is smaller than the current end point
      if x.[0] > endpoint_cur:
        break
      else:
        segments.pop(0)
      
    
if __name__ == "__main__":
  n = int(sys.stdin.readline())
  segs = list()
  for i in range(n):
    
    # create tuple of each segment where 1st element is start point
    # and 2nd element is end point
    seg = tuple(map(int, sys.stdin.readline().split()))
    segs.append(seg)
  # sort the list of points by the endpoint
  segs.sort(key = lambda tup:tup[1])
  # create global variables to store the results
  global count = 0
  global position = list()
  m, position = get_min_points_to_cover_segments(n, segs)
  print(m)
  for x in position:
    print(x, end="")
  
  
  
    
    
    
    
    
