class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        sol = nums[0] + nums[1] + nums[2]
        nums.sort()
        for i in range(len(nums)-2):
            if nums[i] == nums[i-1] and i > 0:
                continue
            j = i+1
            k = len(nums)-1
            while j<k:
                temp = nums[i]+ nums[j] + nums[k]
                if temp == target:
                    return temp
                if abs(sol-target) > abs(temp-target):
                    sol = temp
                if temp < target:
                    j+=1
                else:
                    k-=1
        return sol