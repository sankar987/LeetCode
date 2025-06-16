class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if nums[-1] < target:
            return len(nums)
        for i,v in enumerate(nums):
            if v== target or v > target:
                return i