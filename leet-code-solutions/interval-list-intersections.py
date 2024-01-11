class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i = 0
        j = 0
        res = []
        while i < len(firstList) and j < len(secondList):
            x = max(firstList[i][0], secondList[j][0])
            y = min(firstList[i][1], secondList[j][1])
            if x <= y:
                res.append([x,y])
            if firstList[i][1] < secondList[j][1]:
                i += 1
            else:
                j += 1
            

        return res
                        

