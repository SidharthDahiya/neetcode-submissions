class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        nums.sort()

        for i, a in enumerate(nums):

            if a > 0:
                break
            
            if i > 0 and a == nums[i-1]: # here (a) is nums[i], checking for duplicate (a)
                continue
            
            # now we just follow the process of general 2Sum by fixing the value of (a)
            # where a+b+c = 0 , b = left , c = right

            left = i + 1
            rigth = len(nums) - 1

            while left < rigth:

                threeSum = a + nums[left] + nums[rigth]

                if threeSum < 0:
                    left += 1
                elif threeSum > 0:
                    rigth -= 1
                
                else:
                    res.append([a, nums[left], nums[rigth]])
                    left += 1
                    rigth -= 1

                    while left < rigth and nums[left] == nums[left-1]:
                        left += 1
            
        return res



