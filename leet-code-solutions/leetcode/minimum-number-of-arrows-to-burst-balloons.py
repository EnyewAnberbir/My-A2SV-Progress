class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        count = 0
        the_arrow = float("-inf")

        for point in sorted(points, key=lambda x: x[1]):
            if point[0] > the_arrow:
                count += 1
                the_arrow = point[1]

        return count
        
        


        