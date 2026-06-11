from collections import Counter

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # Step 1: Count the frequency of each number
        count = Counter(nums)
        
        # Step 2: Create buckets where index = frequency
        # We need len(nums) + 1 because a number can appear up to len(nums) times
        freq_buckets = [[] for _ in range(len(nums) + 1)]
        
        # Populate the buckets
        for num, freq in count.items():
            freq_buckets[freq].append(num)
            
        # Step 3: Gather the top k elements by reading buckets backward
        result = []
        for i in range(len(freq_buckets) - 1, 0, -1):
            for num in freq_buckets[i]:
                result.append(num)
                if len(result) == k:
                    return result