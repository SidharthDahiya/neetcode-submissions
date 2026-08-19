class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for num in nums:
            count[num] += 1

        # Sort keys based on count[num] in descending order
        sorted_keys = sorted(count.keys(), key=lambda num: count[num], reverse=True)
        
        # Return the top k elements
        return sorted_keys[:k]