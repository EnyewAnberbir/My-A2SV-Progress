class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort()
        maxnum = 0
        for i in range(len(points)-1):
           maxnum = max(maxnum, (points[i+1][0] - points[i][0]))

        return maxnum

        