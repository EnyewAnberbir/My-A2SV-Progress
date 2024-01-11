class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        def toDict(String):
            sets = {}
            for i in String:
                sets[i] = sets.get(i, 0)+1
            return sets
        sdict = toDict(s[:len(p)-1])
        pdict = toDict(p)
        res = []
        left = 0
        for right in range(len(p)-1, len(s)):
            sdict[s[right]] = sdict.get(s[right], 0)+1
            if sdict == pdict:
                res.append(left)
            sdict[s[left]] -=1
            if sdict[s[left]] == 0:
                del sdict[s[left]]
            left+=1
        return res
