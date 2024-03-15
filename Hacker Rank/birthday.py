def birthday(s, d, m):
    total_count = 0

    for num in s:
        if num[d] + num[d] == len(m):
            total_count += 1
        else:
            return None


# psuedocode

# check the length of the chocolate bar s =[array of numbers]
# check length of the day d=int
# check length of month to find how many indexes needed to add with m=int
#
# iterate through loop by checking first value with second value
#           if sum equals length of day
# return count by +1 to the variable to count how many times chocolate can be split
#           if sum not equal length of day
# continue iteration until array is exhausted and return total count of combination splits to
# total count variable
# return total count


def birthday(s, d, m):
    # count of total combos that resolve solution
    total_count = 0
    # if the length of the chocolate bar is large enough to split be seeing if len(s) is less than the month
    if len(s) < m:
        return 0
    # iterate through the segments of the chocolate bar
    # len(s) - m + 1) gives the length of chocolate bar
    #        -m + 1 calculates starting point
    #           +1 allows to contian entire length of array
    for i in range(len(s) - m + 1):

        # this calculates the sum of the integers in the selected segment,
        # adds all the numbers and gives total sum of segments
        segment_sum = sum(s[i : i + m])

        #   check if segement is equal to the value of the day
        if segment_sum == d:
            #   if true add a count of 1 to the total_count variable that tally's the total count
            total_count += 1
    return total_count


def birthday(s, d, m):
    total_count = 0

    if len(s) < m:
        return 0
    for i in range(len(s) - m + 1):
        segment_sum = sum(s[i : i + m])
        if segment_sum == d:
            total_count += 1
        return total_count


def birthday(s, d, m):
    total_count = 0

    if len(s) < m:
        return 0
    for i in range(len(s) - m + 1):
        segment_sum = sum(s[i : i + m])
        if segment_sum == d:
            total_count = +1
        return total_count
