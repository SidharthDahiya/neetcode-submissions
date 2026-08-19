class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = [0]*3

        # Pass 1: Frequency map
        for num in nums:
            count[num] += 1

        # Pass 2: In-place overwrite
        index = 0
        for i in range(3):
            while count[i] > 0:
                nums[index] = i
                count[i] -= 1
                index += 1


