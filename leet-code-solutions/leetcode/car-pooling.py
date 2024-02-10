class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        prefix_sum = [0] * 1001
        coll = 0
        for numPass, begin, end in trips:
            prefix_sum[begin] += numPass
            prefix_sum[end] -= numPass

        for i in prefix_sum:
            coll += i
            if coll > capacity:
                return False

        return True