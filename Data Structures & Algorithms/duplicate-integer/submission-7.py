class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        mapping = {}

        for i in range(0, len(nums)):
            if nums[i] in mapping:
                return True
            else:
                mapping[nums[i]] = 1
        return False