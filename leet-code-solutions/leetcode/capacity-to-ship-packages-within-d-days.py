class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        a= max(weights)
        def counter(num):
            count = 1
            summ = 0
            for i in range(len(weights)):
                summ += weights[i]
                if summ > num:
                    summ = weights[i]
                    count+=1
            if count > days:
                return False
            return True
        low = a
        high = sum(weights)
        while low < high:
            mid = (low + high)//2
            if counter(mid):
                high = mid
            elif not counter(mid):
                low = mid + 1
            
        return low
      
        
                
        