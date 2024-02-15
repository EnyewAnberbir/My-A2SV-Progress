class Solution:
    def longestPalindrome(self, s: str) -> int:
        sets = Counter(s)
        count = 0
        for val in sets.values():
            if val %2 == 0:
                count += val
            else:
                count += (val-1)
        if count < len(s):
            count+=1
        return count
            













