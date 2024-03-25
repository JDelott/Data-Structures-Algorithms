from typing import List


# class Solution:
#     def getConcatenation(self, nums: List[int]) -> List[int]:
#         # create variable to contain the concatenated list
#         concanated_list = []
#         # iterate through list of nums, and add current index to back of list until compeleted
#         for i in range(len(nums)):
#             concanated_list.append(nums[i])
#         return concanated_list


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []

        for num in nums:
            ans.append(num)

        for num in nums:
            ans.append(num)

        return ans


Solution = Solution()
print(Solution.getConcatenation([1, 2, 1]))
