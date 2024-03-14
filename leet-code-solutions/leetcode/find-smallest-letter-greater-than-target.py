class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left = 0
        right = len(letters)-1
        if ord(letters[right]) <= ord(target):
            return letters[0]
        
        while left < right:
            mid = left + (right-left)//2
            if ord(letters[mid]) <= ord(target):
                left = mid +1
            else:
                right = mid
            
        return letters[left]
        

        