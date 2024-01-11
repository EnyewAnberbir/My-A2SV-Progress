class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        ref = ["a","e","i","o","u"]
        def toDict(string):
            sets = {}
            for i in string:
                sets[i] = sets.get(i, 0)+1
            return sets
        temp = toDict(s[:k-1])
        maxval = 0
        left = 0
        for right in range(k-1, len(s)):
            count = 0
            temp[s[right]] = temp.get(s[right], 0)+1
            for i in temp:
                if i in ref:
                    count += temp[i]
            maxval = max(maxval, count)
            temp[s[left]] -= 1
            if temp[s[left]] == 0:
                del temp[s[left]]
            left+=1
        return maxval

            
        