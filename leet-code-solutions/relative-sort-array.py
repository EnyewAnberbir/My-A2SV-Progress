class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr1.sort(key = lambda x: arr2.index(x) if x in arr2   else len(arr2)+x )

        return arr1

            
        

        