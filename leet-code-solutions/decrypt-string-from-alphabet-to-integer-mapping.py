class Solution:
    def freqAlphabets(self, s: str) -> str:
        coll = ""
        i = len(s) - 1

        while i >= 0:
            if s[i] == '#':
                num = int(s[i-2:i])
                coll = chr(ord('a') + num - 1) + coll
                i -= 3
            else:
                coll = chr(ord('a') + int(s[i]) - 1) + coll
                i -= 1

        return coll
                    