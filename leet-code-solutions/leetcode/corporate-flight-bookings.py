class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        coll = [0]*(n+1)    
        for num1, num2, num3 in bookings:
            coll[num1-1] += num3
            coll[num2] -= num3 
        temp = coll[0]    
        prefix_sum = [temp]            
        for i in range(1,len(coll)-1):
            prefix_sum.append(prefix_sum[i-1] + coll[i] ) 
        return prefix_sum






































# coll=[0]*n,for each in book coll[each[0]-1]+= each[2] if coll[1]<n coll[each[1]]-= each[2]
# for each range(1-n):
#     coll[each]+=coll[each-1]
#     return coll




