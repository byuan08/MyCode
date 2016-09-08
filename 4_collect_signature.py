#! python3
import sys

def get_min_points_to_cover_segments(segments):
    if len(segments) > 0:
        endpoint_cur = segments.pop(0)[1]
        position = list()
        position.append(endpoint_cur)

        for x in segments:
            # Only check the points whose start point is smaller than the current end point
            if x[0] > endpoint_cur:
                continue
            # These segments are covered by current point
            # Remove them from future consideration
            else:
                segments.remove(x)
        return position + get_min_points_to_cover_segments(segments)

    else:

        return []
      
    
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

    position = get_min_points_to_cover_segments(segs)
    print(len(position))
    print("list is ", position)
    for x in position:
        print(x, end=' ')
       
  
  
  
    
    
    
    
    
