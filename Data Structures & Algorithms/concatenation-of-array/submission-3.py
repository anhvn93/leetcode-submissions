class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        arr = [None] *(n*2)
        for i in range(len(nums)):
            arr[i]= nums[i]
            arr[i+n] = nums[i]
        return arr