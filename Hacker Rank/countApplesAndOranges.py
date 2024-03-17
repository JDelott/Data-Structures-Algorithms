# def countApplesAndOranges(s,t,a,b,apples,oranges):
# find the value of the start of house(s)
# fnd the value of the end of the house(t)
# find the value of the Apple tree location(a)
# find the value of the orange tree location(b)
# find value of the apple tree unit distances array [int]
# find the valuie of the orange tree unit distances array [int]

# find sum of location of apple tree (a) + each index value of the apple tree array
# find sum of the location of orange tree(b) + each index value of the orange tree array

# find value that is with in the range of the start of house(s) and end of house(t)
# compare value of sum of a + apples
# if a value is within range of the house
# count of apples hitting the house increases +1

# compare value of sum of b + oranges
# if b value is within the range of the house
# count of oranges hitting the house increases +1

# result will be number of apples hitting house and number of oranges hitting the house


# def countApplesAndOranges(s, t, a, b, apples, oranges):
#     total_apples = 0
#     total_oranges = 0

#     for i in apples:
#         sum_apples = apples + [i]
#         for j in oranges:
#             sum_oranges = oranges = [j]
#     if sum_apples == range(s + t):
#         return total_apples + 1
#     if sum_oranges == range(s + t):
#         return total_oranges + 1


def countApplesAndOranges(s, t, a, b, apples, oranges):
    # create variable to hold count of apples
    total_apples = 0
    # create variable to hold count of oranges
    total_oranges = 0
    # iterate of the array of apples
    for apple in apples:
        # find the distance of a + apple
        distance = a + apple
        # check if start of house (s) is less than or equal to end of house(t)
        if s <= distance <= t:
            total_apples += 1
    # iterate over the array of oranges:
    for orange in oranges:
        # find distance of b + oranges
        distance = b + orange
        # check if start of house (s) is less than or equal to end of house(t)
        if s <= distance <= t:
            total_oranges += 1

    return total_apples, total_oranges


s = 7
t = 11
a = 5
b = 15
apples = [2, -2, 7]
oranges = [-5, 10, 15]

apple_hits, orange_hits = countApplesAndOranges(s, t, a, b, apples, oranges)
print("Apples:", apple_hits)
print("Oranges:", orange_hits)
