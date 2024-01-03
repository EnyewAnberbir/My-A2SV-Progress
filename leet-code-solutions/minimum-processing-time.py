class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        a = len(processorTime)
        b = len(tasks)
        tasks.sort()
        processorTime.sort()
        i=0 
        temp = 0
        for j in range(b-1, -1, -4):
            temp = max(temp, (tasks[j] + processorTime[i]))
            i+=1

        return temp

# [121,99]

# [287,315,293,260,333,362,69,233]

    