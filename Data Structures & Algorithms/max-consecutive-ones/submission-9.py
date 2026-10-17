class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        outer = local = 0
        for e in nums:
            if e == 1:
                local += 1
            else:
                outer = max(outer, local)
                local = 0
        return max(outer, local)

            
        