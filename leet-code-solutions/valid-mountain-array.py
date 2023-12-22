class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        count = 0
        for i in range(len(arr)-1):
            if arr[i] == arr[i+1]:
                return False
            if arr[i] < arr[i+1]:
                count += 1
            
            
        if len(arr) - count <2 or count == 0 : 
            return False
            
        check1 = arr[:count+1]
        check2 = arr[count:] [::-1]

        return check1 == sorted(check1) and check2 == sorted(check2)
        
            
        

           



            

        