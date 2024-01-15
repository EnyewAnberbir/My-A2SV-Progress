class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left, maxlen, countmax = 0 ,0 ,0
        coll = {}
        for right in range(len(s)):
            coll[s[right]] = coll.get(s[right], 0)+1
            countmax = max(countmax, coll[s[right]])
            if (right-left+1) - countmax > k:
                coll[s[left]] -= 1
                if coll[s[left]] ==0:
                    del coll[s[left]]
                left+=1
            maxlen = max(maxlen , right-left+1)
        return maxlen
        