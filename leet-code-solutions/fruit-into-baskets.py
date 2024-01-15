class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left, maxval = 0, 0
        myDict = {}
        for right in range(len(fruits)):
            if fruits[right] not in myDict:
                myDict[fruits[right]] =0
            myDict[fruits[right]] +=1
            while len(myDict) > 2:
                myDict[fruits[left]] -= 1
                if myDict[fruits[left]] == 0:
                    del myDict[fruits[left]]
                left += 1
            maxval = max(maxval, right-left+1)
        return maxval
        