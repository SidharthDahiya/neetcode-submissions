class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res = defaultdict(int)
        maxx = 0
        result = 0

        for num in nums:
            res[num] += 1
        
        for num in res:
            if res[num] > maxx:
                maxx = res[num]
                result = num
        
        return result
