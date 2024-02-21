class Solution:
    def reverseString(self, s: List[str]) -> None:
        def recursive(arr, idx):
            if idx == len(s)//2:
                arr[idx] = arr[idx]
            else:
                arr[idx] , arr[len(s)-idx-1] = arr[len(s)-idx-1] , arr[idx]

                recursive(arr,idx+1)
        return recursive(s, 0)
       


         

        