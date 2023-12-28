class Solution:
    def sortSentence(self, s: str) -> str:
        check = s.split(" ")
        check.sort(key = lambda x: x[-1])
        temp = []
        for i in check:
            temp.append(i[:len(i)-1])
        res = " ".join(temp)
        return res
            