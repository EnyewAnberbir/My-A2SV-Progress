class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        result = []
        ref = [set('qwertyuiop'), set('asdfghjkl'), set('zxcvbnm')]

        for word in words:
            toLower = set(word.lower())
            if any(toLower <= row for row in ref):
                result.append(word)

        return result
            
                    



        