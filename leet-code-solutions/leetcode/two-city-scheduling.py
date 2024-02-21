class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        res = []
        idx = 0
        for a,b in costs:
            res.append([a-b, idx])
            idx+=1

        res.sort()
        i = 0
        j = len(res)-1
        summ = 0
        while i <j:
            summ += costs[res[i][1]][0]
            summ += costs[res[j][1]][1]
            i+=1
            j-=1
        return summ


