class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        ans = float("inf")
        myDict = {}

        for i, c in enumerate(cards):
            if c in myDict:
                ans = min(ans, i - myDict[c] + 1)
            myDict[c] = i

        if ans == float("inf"):
            return -1
        else:
            return ans
                    
            
            
            

        