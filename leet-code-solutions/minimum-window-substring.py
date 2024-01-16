class Solution:
    def minWindow(self, s: str, t: str) -> str:
        dict1 = {}
        dict2 = {}

        for char in t:
            dict1[char] = dict1.get(char, 0) + 1
        left, right = 0, 0
        min_length = float('inf')
        min_win = ""
        x = len(dict1)
        count = 0

        while right < len(s):
            char = s[right]
            dict2[char] = dict2.get(char, 0) + 1
            if char in dict1 and dict2[char] == dict1[char]:
                count += 1
            while count == x and left <= right:
                if right - left + 1 < min_length:
                    min_length = right - left + 1
                    min_win = s[left:right + 1]
                left_char = s[left]
                dict2[left_char] -= 1
                if left_char in dict1 and dict2[left_char] < dict1[left_char]:
                    count -= 1
                left += 1

            right += 1

        return min_win
        