class Solution:
    def balancedString(self, s: str) -> int:
        ans = len(s)
        count = collections.Counter(s) 
        j = 0

        for i, element in enumerate(s):
            count[element] -= 1
            while j < len(s) and all(count[element] <= len(s) // 4 for element in 'QWER'):
                ans = min(ans, i - j + 1)
                count[s[j]] += 1
                j += 1

        return ans