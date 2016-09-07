import sys

def get_min_points_to_cover_segments(n, segments):
  if len(segments) > 0:
    endpoint_cur = segments.pop()[1]
    # Only check the points whose start point is smaller than the current end point
    i = 0
    for x in range(1:n-1)
      count++
      position.append(endpoint_cur)
      i++
    
    n = n-i
      
      
    
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
  
  
  
    
    
    
    
    
