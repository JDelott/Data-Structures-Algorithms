from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # create a dictionary to conatain the indexes previously seen
        num_dict = {}
        for index, num in enumerate(nums):

            complement = target - num
            # calculate the compliments to see which values equal target
            if complement in num_dict:
                # if the compliment exists and is eqaul to target return num_dict
                return [num_dict[complement], index]
            num_dict[num] = index
            # if no compliment return empty array
        return []


solution = Solution()
print(solution.twoSum([1, 2, 1], target=5))


# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         result = []
#         for num in nums:
#             if num[0] + num[1] == target:
#                 result.append(num[0], num[1])
#         return result


# # nums = [1, 2, 3]
# # target = 5

# Solution = Solution()
# print(Solution.twoSum([1, 2, 1], target=5))

# loop through the numbers and
# find the two numbers that equal the target number
# return index array if the two indexes that equal target number
