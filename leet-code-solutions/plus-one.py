class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        coll = ""
        coll1 = []
        for i in range(len(digits)):
            coll += str(digits[i])
        temp = int(coll) +1
        for i in str(temp):
            coll1.append(int(i))
        return coll1

        

        
        