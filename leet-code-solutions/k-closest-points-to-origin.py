import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res =[]
        points.sort(key = lambda x: (x[0])**2 + (x[1])**2)
        print(points)
        for i in range(k):
            res.append(points[i])

        return res
            
        


            




        