class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        left = 0
        rigth = len(numbers) - 1

        while left < rigth:

            sum = numbers[left] + numbers[rigth]

            if sum < target:
                left += 1
            
            elif sum > target:
                rigth -= 1

            else:
                return [left + 1, rigth + 1]

        return []

