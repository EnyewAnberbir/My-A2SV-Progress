class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        canmax = max(candies)
        return [candy + extraCandies >= canmax for candy in candies]

         