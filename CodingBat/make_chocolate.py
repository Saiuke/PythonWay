#
# We want make a package of goal kilos of chocolate.
# We have small bars (1 kilo each) and big bars (5 kilos each).
# Return the number of small bars to use, assuming we always use big bars before small bars.
# Return -1 if it can't be done.
#

def make_chocolate(small, big, goal):
    totalBig = big * 5
    if totalBig + small < goal or small < goal % 5:
        return -1
    smallNeeded = goal - totalBig
    if smallNeeded < 0:  # Will happen when the goal is less than 5. For example in make_chocolate(4, 1, 4)
        return smallNeeded % 5
    else:
        return smallNeeded



