class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        count = 0
        i = len(nums)-1
        start = nums[i]
        while i >= 1:   
            no_space = ceil(nums[i-1]/start)
            print(no_space)
            count += no_space-1
            start = nums[i-1]//no_space
            i-=1
        
        return count
 



            


# [12,9,7,6,17,19,21]

        