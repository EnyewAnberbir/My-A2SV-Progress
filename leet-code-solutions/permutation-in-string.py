class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def toDict(string):
            coll = {}
            for i in range(len(string)):
                coll[string[i]] = coll.get(string[i], 0)+1
            return coll
        temp1 = toDict(s1)
        temp2 = toDict(s2[:len(s1)-1])

        for right in range(len(s1)-1, len(s2)):
            temp2[s2[right]] = temp2.get(s2[right], 0)+1
            if temp1 == temp2:
                return True
            temp2[s2[right-len(s1)+1]] -= 1
            if temp2[s2[right-len(s1)+1]] == 0:
                del temp2[s2[right-len(s1)+1]]
        return temp1 == temp2
        