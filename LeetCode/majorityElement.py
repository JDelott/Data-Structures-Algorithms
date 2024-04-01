from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        result = []
        for num in range(nums):
            if len(num) == num > nums:
                result.append(num)
        return result
