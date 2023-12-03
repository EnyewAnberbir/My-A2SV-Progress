class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        myDict = {char: i for i, char in enumerate(order)}
        
        def compare(word1, word2):
            for i in range(min(len(word1), len(word2))):
                if myDict[word1[i]] < myDict[word2[i]]:
                    return True
                elif myDict[word1[i]] > myDict[word2[i]]:
                    return False
            return len(word1) <= len(word2)
        
        for i in range(1, len(words)):
            if not compare(words[i-1], words[i]):
                return False
        
        return True
        