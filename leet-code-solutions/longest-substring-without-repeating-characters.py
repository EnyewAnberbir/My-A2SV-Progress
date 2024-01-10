class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ourDict = {}
        length = 0
        l = 0
        
        for j in range(len(s)):
            if s[j] in ourDict and ourDict[s[j]] >= l:
                l = ourDict[s[j]]+1
            ourDict[s[j]] = j


            length = max(length, j-l+1)
        return length


