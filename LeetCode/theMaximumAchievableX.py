class Solution:
    def theMaxAchievableX(self, num: int, t: int) -> int:
        result = []
        for i in range(num):
            res = (i + 1) * t
            total_value = res + t
            result.append(total_value)
        return result[-1]


solution = Solution()
print(solution.theMaxAchievableX(5, 2))
# psuedocode

# find the value of num
# find the value of time (t)
# add +1 to num as many times t is equal to
# find total value of num after final +1 increment based on t
# add final num value + the value of t to get value of x
# sum of final value of num and t = x
# x = achievable
