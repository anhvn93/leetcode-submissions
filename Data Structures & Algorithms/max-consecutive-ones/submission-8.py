class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max = 0
        local = 0
        if len(nums) >1:
            for i in range(len(nums)):
                if nums[i]==1:
                    local += 1
                    if local > max:
                        max += 1
                else :
                    local = 0
        else:
            if nums[0] == 1:
                return 1
        return max

            
        