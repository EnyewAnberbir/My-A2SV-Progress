class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        def get_next_index(curr_index):
            return (curr_index + nums[curr_index]) % len(nums)

        for i in range(len(nums)):
            if nums[i] == 0:
                continue

            slow = i
            fast = i
            while nums[slow] * nums[get_next_index(slow)] > 0 and nums[fast] * nums[get_next_index(fast)] > 0:
                slow = get_next_index(slow)
                fast = get_next_index(get_next_index(fast))

                if slow == fast:
                    if slow == get_next_index(slow):
                        break
                    return True
            slow = i
            while nums[slow] * nums[get_next_index(slow)] > 0:
                temp = slow
                slow = get_next_index(slow)
                nums[temp] = 0

        return False