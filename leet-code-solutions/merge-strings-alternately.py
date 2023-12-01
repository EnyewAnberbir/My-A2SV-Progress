class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        coll = ""
        i = 0
        j = 0
        if len(word1) == len(word2):
            while i < len(word1) and j < len(word2):
                coll += word1[i]
                coll += word2[j]
                i+=1
                j+=1
        elif len(word1) > len(word2):
            while i < len(word1[:len(word2)]) and j < len(word2):
                coll += word1[i]
                coll += word2[j]
                i+=1
                j+=1
            coll += word1[len(word2):]
        else:
            while i < len(word1) and j < len(word2[:len(word1)]):
                coll += word1[i]
                coll += word2[j]
                i+=1
                j+=1
            coll += word2[len(word1):]
        return coll

        

        