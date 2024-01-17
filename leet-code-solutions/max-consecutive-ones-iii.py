class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        i, j = 0, 0
        answer =float('-inf')
        while j<len(nums) and i<len(nums):
            if nums[j] != 1:   
                if k>0:
                    k-=1
                else:
                    while k<0 or nums[i]==1:
                        if nums[i]==0:
                            k+=1
                        i+=1
                    i+=1
            answer =max(answer ,j-i+1)  
            j+=1
        return answer 