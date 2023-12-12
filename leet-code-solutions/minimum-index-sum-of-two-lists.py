class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        sets = set(list1) & set(list2)  
        idx = {}

        for cmn in sets:
            index_sum = list1.index(cmn) + list2.index(cmn)
            idx[cmn] = index_sum

        min_summ = min(idx.values())
        result = [cmn for cmn, index_sum in idx.items() if index_sum == min_summ]

        return result

        