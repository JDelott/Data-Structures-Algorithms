# def divisibleSumPairs(n,k,ar):


# psuedo code

# identify value of n which is the total length of the ar array

# identify value of k which is the number that the ar array will be divided by

# identify the the ar array which is the list of numbers that are ar values

# check ar indexes that are divisible by 3

# total count of index combinations divisible by 3

# return total count


# def divisibleSumPairs(n, k, ar):
#     total = 0
#     n = len(ar)

#     for num in ar:
#         if num[0] + num[1] % 3:
#             return total.append(num)

#     return total


def divisibleSumPairs(n, k, ar):
    total = 0
    n = len(ar)

    for i in range(n):
        for j in range(i + 1, n):
            if (ar[i] + ar[j]) % k == 0:
                total += 1
    return total


result = divisibleSumPairs(6, 3, [2, 31, 4, 5, 6, 7])
print(result)
