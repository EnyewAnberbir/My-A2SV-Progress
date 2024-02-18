class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_len = 0
        ans = ""
        for right in range(len(s)):
            left = 0
            while left <= right:     
                if s[left:right+1] == s[left:right+1][::-1]:
                    if max_len < right-left+1:
                        max_len = right-left+1
                        ans = s[left:right+1]
                left+=1
        return ans


        