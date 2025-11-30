from typing import List

# Brute force, with O(nlogn)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums.sort()

        longest = 1
        current = 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                current += 1
            elif nums[i] == nums[i - 1]:
                continue
            else:
                longest = max(longest, current)
                current = 1

        return max(longest, current)

# NeetCode solution with O(n)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for n in numSet:
            if n - 1 not in numSet:
                length = 0
                while n + length in numSet:
                    length += 1
                longest = max(longest, length)
        
        return longest