class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        ans = []

        for i in range(len(arr), 0, -1):
            idx = arr.index(i) 
            arr[:idx + 1] = arr[:idx + 1][::-1]
            arr[:i] = arr[:i][::-1]
            ans.append(idx + 1)
            ans.append(i)

        return ans
