class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        arr = [1]
        def helper(arr,rowInd):
            res= []
            if rowInd == rowIndex:
                return arr
            for i in range(len(arr)-1):
                res.append(arr[i] + arr[i+1])
            res =  [1] + res + [1]
            return helper(res, rowInd+1)

        return helper(arr, 0)
        
         