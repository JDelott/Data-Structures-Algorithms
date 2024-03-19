# pseudocode

# input process
# check number of steps on the hike(steps)
# check the string that descripes the path (path)

# iterate throught the steps
# add +1 if path is U
# subtract -1 if path is D

# check if final step is at sea level
# if yes return +1 to variable count
# if not find value of  how many valleys from the decreaseing path


# def countingValleys(steps, path):
#     total_valleys = 0

#     for i in steps:
#         if i == "D":
#             path = path + 1
#         if i == "U":
#             path = path - 1
#         total_valleys = path

#         return total_valleys


def countingValleys(steps, path):
    # handle steps and path input incase of improper input
    if len(steps) != len(path):
        return -1
    # create variable to have the altitude count
    altitude = 0
    # create variable to count total_valleys
    total_valleys = 0
    # create variable to count in_valley
    in_valley = 0

    # iterate over steps in path
    for step in path:
        # check if step is == "U":
        if step == "U":
            # add count +1 to altitude variable
            altitude += 1
        # check if step is == "D"
        if step == "D":
            #  subtract count -1 from altidude variable
            altitude -= 1

            # check if altitude is less than 0 and not in_vally(boolean):
            if altitude < 0 and not in_valley:
                # set in_valley variable to True
                in_valley = True
            # check if altitude is equal to 0 and in_valley
            elif altitude == 0 and in_valley:
                # set total_valleys variable count +1
                total_valleys += 1
                # set in_valley to True
                in_valley = False
    return total_valleys


steps = "8"
path = "UUDDUDUU"

result = countingValleys(steps, path)
print(result)
