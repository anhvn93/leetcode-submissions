class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maximum = local = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                local = 0
            else:
                local += 1
                maximum = max(local, maximum)
        return maximum