class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        arr = [0]* len(temperatures)
        stack = []
        for i ,t in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < t:
                curr = stack.pop()
                arr[curr] = i- curr
                
            stack.append(i)
        return arr
                


        