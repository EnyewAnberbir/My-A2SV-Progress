class Solution:
    def printVertically(self, s: str) -> List[str]:
        x = s.split()
        max_len = max(len(word) for word in x)
        res = []

        for i in range(max_len):
            col = ''
            for word in x:
                if i < len(word):
                    col += word[i]
                else:
                    col += ' '
            res.append(col.rstrip())

        return res