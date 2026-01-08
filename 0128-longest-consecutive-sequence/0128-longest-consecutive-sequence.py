from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Handle edge case where nums is empty
        if not nums:
            return 0
        
        # Step 1: Put all numbers into a set (O(n) time)
        nums_set = set(nums)
        max_length = 0
        
        # Step 2: Iterate over each number in the set
        for num in nums_set:
            # Only start counting from num if it's the start of a sequence
            if num - 1 not in nums_set:
                current_num = num
                current_length = 1
                
                # Count how long the consecutive sequence is
                while current_num + 1 in nums_set:
                    current_num += 1
                    current_length += 1
                
                # Update max length found so far
                max_length = max(max_length, current_length)
        
        return max_length
