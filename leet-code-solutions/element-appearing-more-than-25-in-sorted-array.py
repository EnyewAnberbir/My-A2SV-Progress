class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)
        target = n // 4

        for i in range(n - target):
            if arr[i] == arr[i + target]:
                return arr[i]

        