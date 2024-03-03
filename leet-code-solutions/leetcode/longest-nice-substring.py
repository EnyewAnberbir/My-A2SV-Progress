class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        if len(s) < 2:
            return ""
        
        mySet = set(s)
        for i,c in enumerate(s):
            if c.swapcase() not in mySet:
                part1 = self.longestNiceSubstring(s[0:i])
                part2 = self.longestNiceSubstring(s[i+1:])

                if len(part2) > len(part1):
                    return part2
                else:
                    return part1
        return s