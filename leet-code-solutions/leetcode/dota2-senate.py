class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        queue1 = deque()
        queue2 = deque()
        for i , char in enumerate(senate):
            if char == "D":
                queue1.append(i)
            else:
                queue2.append(i)
        length = len(senate)
        while queue2 and queue1:
            if queue1[0] < queue2[0]:
                queue2.popleft()
                poped = queue1.popleft()
                queue1.append(poped+length)
            else:
                queue1.popleft()
                poped = queue2.popleft()
                queue2.append(poped+length)
        
        if queue2:
            return "Radiant"
        else:
            return "Dire"