class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        arr = [0] * len(s)
        for i in range(len(s)):
            arr[indices[i]] = s[i]

        string =""
        for i in range(len(arr)):
            string += str(arr[i])
        
        return string
