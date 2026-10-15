class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        numsSetTuple = tuple(set(nums))
        numsTuple = tuple(nums)

        if len(numsSetTuple) == len(numsTuple):
            return False
        else:
            return True
