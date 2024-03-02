class Solution:
    def sumSubarrayMins(self, arr: list[int]) -> int:
        stack = []
        total = 0
        for i in range(len(arr)+1):
            while i == len(arr) or (stack and arr[i] < stack[-1][0]):
                top = stack.pop()
                right = i - top[1]
                left = 1
                if stack:
                    left = top[1] - stack[-1][1]
                else:
                    left = top[1] + 1
                tmp = right * left if left else right
                total += top[0] * tmp
                if i == len(arr) and not stack:
                    break
            if i < len(arr):               
                stack.append([arr[i], i])
        return total % (10**9 + 7)