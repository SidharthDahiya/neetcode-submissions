class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        res = {}

        for i in range(len(numbers)):
            current = numbers[i]
            compliment = target - current

            if compliment in res:
                return [res[compliment] + 1 , i + 1]
            
            res[current] = i 